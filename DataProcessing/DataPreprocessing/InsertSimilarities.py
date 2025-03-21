from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity
import os

from .VectorizeBooks import GetTermFrequencyMatrix
from .Similarities import InsertSimilarBooks

if __name__ == "__main__":
    # Setting up the connection with MongoDB
    ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
    BooksDB = ClientDatabase[os.getenv("DB_NAME")]
    BooksCollection = BooksDB.BooksCollection

    # Getting book
    DataBooks = list(BooksCollection.find({}))

    # Getting cosine similarity between books
    TermFrequency_InverseDocumentFrequency = GetTermFrequencyMatrix(DataBooks)
    books_similarity = cosine_similarity(TermFrequency_InverseDocumentFrequency,TermFrequency_InverseDocumentFrequency)

    # Inserting similar books at each book
    InsertSimilarBooks(DataBooks,books_similarity,BooksCollection)

    ClientDatabase.close()