from pymongo import MongoClient
import os

# Setting up the connection with MongoDB
ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
BooksDB = ClientDatabase[os.getenv("DB_NAME")]
BooksCollection = BooksDB.BooksCollection

def GetRandomBooks() -> list[dict]:
    return list(BooksCollection.aggregate([{"$sample":{"size":3}}]))