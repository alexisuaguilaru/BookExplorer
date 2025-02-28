from pymongo import MongoClient
import os

if __name__ == "__main__":
    ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
    BooksDB = ClientDatabase[os.getenv("DB_NAME")]
    BooksCollection = BooksDB.BooksCollection

    for book_example in BooksCollection.aggregate([{"$sample":{"size":3}}]):
        print(book_example,'\n')