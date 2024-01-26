from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
CORS(app, support_credentials=True)

def find_similar_documents(input_text, tfidf_vectorizer, tfidf_vectorized_data, result_df):
    input_tfidf_vector = tfidf_vectorizer.transform([input_text]).toarray()
    similarities = cosine_similarity(input_tfidf_vector, tfidf_vectorized_data)
    top_indices = np.argsort(similarities[0])[::-1][:5]
    similar_documents = result_df.iloc[top_indices]
    return similar_documents

tfidf_vectorizer = pickle.load(open("tfidf_vectorizer.pkl", 'rb'))
tfidf_vectorized_data = pickle.load(open("tfidf_vectorized_data.pkl", 'rb'))
result_df = pickle.load(open('result_df.pkl', 'rb'))

@app.route("/")
def home():
    return "Connected to Backend of RBI Chat Bot"

@app.route("/query", methods=['GET'])
@cross_origin(supports_credentials=True)
def query():
    tokenId = request.args.get('tokenId')
    query = request.args.get('query')
    noOfResult = request.args.get('limit')

    if request.method == 'GET':
        if tokenId != "":
            # Call the find_similar_documents function with the provided parameters
            similar_documents = find_similar_documents(query, tfidf_vectorizer, tfidf_vectorized_data, result_df)
            result_json = similar_documents.to_json(orient="records")
            return jsonify(result_json), 200
        else:
            return "Invalid Token Id, Unauthorized access", 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
