import os

from DataProcessing import GetBook

subjects = ['fiction','fantasy','historical_fiction',
            'horror','humor','literature','magic',
            'mystery_and_detective_stories','plays',
            'poetry','romance','science_fiction',
            'short_stories','thriller','young_adult_fiction']
def InsertBooksIntoCollection(BooksCollection:object) -> None:
    """
        Function for inserting books into 
        MongoDB collection

        -- BooksCollection : object :: MongoDB collection where the books are inserted
    """
    for book in GetBook(subjects,int(os.getenv("AMOUNT_BOOKS"))):
        BooksCollection.insert_one(book)