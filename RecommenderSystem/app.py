from flask import Flask , request , jsonify
from pymongo import MongoClient
import os

from Recommender.Recommendations import GetRecommendations

# Setting up the connection with MongoDB
ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
BooksDB = ClientDatabase[os.getenv("DB_NAME")]
BooksCollection = BooksDB.BooksCollection

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/',methods=['GET'])
def index():
    isbn = request.args.get('isbn')
    print(isbn)
    return jsonify(GetRecommendations(isbn,BooksCollection))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8013,debug=bool(os.getenv("DEBUG_MODE")))