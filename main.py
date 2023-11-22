import database_connection
import data_fetching
import recommendation_model
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint for getting recommendations
@app.route('/recommendations', methods=['POST'])
def get_recommendations_api():
    try:
         # Replace these with your database details
        host = 'localhost'
        user = 'root'
        password = ''
        database = 'onlinefoodorder'

        conn, cursor = database_connection.connect_to_database(host, user, password, database)

        # Get data from the API
        api_data = request.get_json()

        # Assuming the API response has a 'description' field and 'food_id'
        api_food_id = api_data.get('food_id', None)
        api_description = api_data.get('description', '')

        # Preprocess data and set up the recommendation model
        fetched_data = data_fetching.fetch_data(cursor)
        processed_data = data_fetching.preprocess_data(fetched_data)

        # Example usage:
        model, tfidf_vectorizer = recommendation_model.build_recommendation_model(processed_data)
        recommendations = recommendation_model.get_recommendations(api_description, model, tfidf_vectorizer, processed_data)

        # Extract food IDs from recommendations
        food_ids = [recommendation[0] for recommendation in recommendations]

        # Remove api_food_id if it exists in the food_ids array
        if api_food_id is not None and api_food_id in food_ids:
            food_ids.remove(api_food_id)

        print(food_ids)

        # Convert the food IDs to a JSON response
        response = jsonify(food_ids)


        return response
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
