from pymongo import MongoClient

from DataProcessing import GetBook

ClientDatabase = MongoClient("mongodb://root:1234@BooksDatabase:27017/")
BooksDB = ClientDatabase.BooksDB
BooksCollection = BooksDB.BooksCollection

subjects = ['fiction','fantasy','historical_fiction',
            'horror','humor','literature','magic',
            'mystery_and_detective_stories','plays',
            'poetry','romance','science_fiction',
            'short_stories','thriller','young_adult_fiction']

for book in GetBook(subjects[:3],10):
    BooksCollection.insert_one(book)

ClientDatabase.close()