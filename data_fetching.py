import mysql.connector
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
nltk.download('punkt')

def fetch_data(cursor):
    cursor.execute("SELECT * FROM tbl_food")
    data = cursor.fetchall()
    return data

def preprocess_data(data):
    # Define NLTK stop words and punctuation
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    # Preprocessing code
    processed_data = []
    for row in data:
        id = row[0]
        title = row[1]
        description = row[2]
        price = row[3]
        image_name = row[4]
        category_id = row[5]
        featured = row[6]
        active = row[7]

        # Lowercase conversion for 'description'
        description = description.lower()

        # Tokenization for 'description'
        tokens = word_tokenize(description)

        # Remove stopwords and punctuation from 'description'
        filtered_tokens = [word for word in tokens if word not in stop_words and word not in punctuation]

        # Join tokens back into a cleaned description
        cleaned_description = ' '.join(filtered_tokens)

        # Append cleaned data to processed_data
        processed_data.append((id, title, cleaned_description, price, image_name, category_id, featured, active))

    return processed_data