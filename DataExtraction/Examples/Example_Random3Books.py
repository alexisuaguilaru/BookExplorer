from pymongo import MongoClient
import os

if __name__ == "__main__":
    # Setting up the connection with MongoDB
    ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
    BooksDB = ClientDatabase[os.getenv("DB_NAME")]
    BooksCollection = BooksDB.BooksCollection

    # Obtaining three random books
    for book_example in BooksCollection.aggregate([{"$sample":{"size":3}}]):
        print(book_example,'\n')