from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity
import os

from .Similarities import InsertSimilarBooks
from .VectorizeBooks import GetTermFrequencyMatrix

def InsertSimilaritiesIntoCollection(BooksCollection:object) -> None:
    """
    Function for precomputing and inserting 
    similar books in each book

    Parameters
    ----------
    BooksCollection : object
        MongoDB collection where the books belong

    Returns
    -------
    `None`
    """
    data_books = list(BooksCollection.find({}))

    term_frequency_inverse_document_frequency = GetTermFrequencyMatrix(data_books)
    books_similarity = cosine_similarity(term_frequency_inverse_document_frequency,term_frequency_inverse_document_frequency)

    InsertSimilarBooks(data_books,books_similarity,BooksCollection)