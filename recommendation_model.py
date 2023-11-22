import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Function to build a recommendation model
def build_recommendation_model(data):
    # Convert the list of descriptions to a DataFrame
    df = pd.DataFrame({'description': [str(item) if isinstance(item, tuple) else item for item in data]})

    # Assuming 'description' is the text feature in your data
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    feature_vectors = tfidf_vectorizer.fit_transform(df['description'])

    model = NearestNeighbors(n_neighbors=5, metric='cosine', algorithm='brute')
    model.fit(feature_vectors)

    return model, tfidf_vectorizer

# Function to get recommendations
def get_recommendations(current_food_item, model, tfidf_vectorizer, data):
    current_item_vector = tfidf_vectorizer.transform([current_food_item])

    # Get the indices of the nearest neighbors
    _, neighbor_indices = model.kneighbors(current_item_vector)

    recommended_food_items = [data[i] for i in neighbor_indices[0]]

    return recommended_food_items
