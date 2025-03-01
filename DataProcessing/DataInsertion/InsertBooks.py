from pymongo import MongoClient
import os

from DataProcessing import GetBook

if __name__ == "__main__":
    # Setting up the connection with MongoDB
    ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
    BooksDB = ClientDatabase[os.getenv("DB_NAME")]
    BooksCollection = BooksDB.BooksCollection
    
    # Extracting books by subject
    subjects = ['fiction','fantasy','historical_fiction',
                'horror','humor','literature','magic',
                'mystery_and_detective_stories','plays',
                'poetry','romance','science_fiction',
                'short_stories','thriller','young_adult_fiction']
    
    for book in GetBook(subjects,int(os.getenv("AMOUNT_BOOKS"))):
        BooksCollection.insert_one(book)

    ClientDatabase.close()