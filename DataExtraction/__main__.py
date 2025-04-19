from pymongo import MongoClient
import os

from DataExtraction import InsertBooksIntoCollection , InsertSimilaritiesIntoCollection

if __name__ == "__main__":
    # Setting up the connection with MongoDB
    ClientDatabase = MongoClient(os.getenv("MONGO_URI"))
    BooksDB = ClientDatabase[os.getenv("DB_NAME")]
    BooksCollection = BooksDB.BooksCollection
    BooksCollection.create_index('isbn',unique=True)
    
    # Extracting and inserting books into collection
    InsertBooksIntoCollection(BooksCollection)

    # Inserting similar books in each book
    InsertSimilaritiesIntoCollection(BooksCollection)

    ClientDatabase.close()