from flask import Flask , request , jsonify
from pymongo import MongoClient
import os

from RecommenderSystem import GetRecommendations , GetInformationBook

# Setting up the connection with MongoDB
ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
BooksDB = ClientDatabase[os.getenv("DB_NAME")]
BooksCollection = BooksDB.BooksCollection

# Setting up the flask app
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/recommendations',methods=['GET'])
def Recommendations():
    isbn = request.args.get('isbn')
    return jsonify(GetRecommendations(isbn,BooksCollection))

@app.route('/information_book',methods=['GET'])
def InformationBook():
    isbn = request.args.get('isbn')
    return jsonify(GetInformationBook(isbn,BooksCollection))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8013,debug=bool(os.getenv("DEBUG_MODE")))