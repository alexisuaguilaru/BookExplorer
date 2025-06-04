import os
from pymongo.errors import DuplicateKeyError

from ..DataExtraction import GetBook

subjects = ['fiction','fantasy','historical_fiction',
            'horror','humor','literature','magic',
            'mystery_and_detective_stories','plays',
            'poetry','romance','science_fiction',
            'short_stories','thriller','young_adult_fiction']
def InsertBooksIntoCollection(BooksCollection:object) -> None:
    """
    Function for inserting books into 
    MongoDB collection

    Parameters
    ----------
    BooksCollection : object
        MongoDB collection where the books are inserted

    Returns
    -------
    `None`
    """
    for book in GetBook(subjects,int(os.getenv("AMOUNT_BOOKS"))):
        try:
            BooksCollection.insert_one(book)
        except DuplicateKeyError as exception:
            continue