"""
DataExtraction
==============

Module with the necessary functions to perform 
extraction, transformation and loading (ETL) of 
data (books) into the database in MongoDB
"""

from .DataInsertion import InsertBooksIntoCollection
from .DataPreprocessing import InsertSimilaritiesIntoCollection