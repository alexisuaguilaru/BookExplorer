from pymongo import MongoClient
import os

from .VectorizeBooks import GetTermFrequencyMatrix

if __name__ == "__main__":
    # Setting up the connection with MongoDB
    ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
    BooksDB = ClientDatabase[os.getenv("DB_NAME")]
    BooksCollection = BooksDB.BooksCollection

    # Getting book
    DataBooks = list(BooksCollection.find({}))

    TermFrequency_InverseDocumentFrecuency = GetTermFrequencyMatrix(DataBooks)
    print(TermFrequency_InverseDocumentFrecuency)

    ClientDatabase.close()