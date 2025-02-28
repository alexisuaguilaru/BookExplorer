from pymongo import MongoClient
import os

from DataProcessing import GetBook

if __name__ == "__main__":
    ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
    BooksDB = ClientDatabase[os.getenv("DB_NAME")]
    BooksCollection = BooksDB.BooksCollection
    
    subjects = ['fiction','fantasy','historical_fiction',
                'horror','humor','literature','magic',
                'mystery_and_detective_stories','plays',
                'poetry','romance','science_fiction',
                'short_stories','thriller','young_adult_fiction']
    
    for book in GetBook(subjects,10):
        BooksCollection.insert_one(book)

    ClientDatabase.close()