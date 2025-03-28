import requests
from random import sample

from typing import Iterable

# Setting routes for accessing of resources (recommended books and their information(data))
API = "http://RecommenderSystem:8013/{resource}?isbn={isbn}"
resource_recommendations = "recommendations"
resource_information = "information_book"
def RecommendedBooks(ISBN:str='') -> Iterable[dict]:
    """
        Function for getting information of 
        recommended books for a some book

        -- ISBN : str :: Book's ISBN whose gets its recommendations
    """
    isbn_books = requests.get(API.format(resource=resource_recommendations,isbn=ISBN)).json()
    for isbn_book in sample(isbn_books,3):
        information_book = requests.get(API.format(resource=resource_information,isbn=isbn_book)).json()
        yield information_book