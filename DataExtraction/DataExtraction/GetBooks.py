import requests
import os

from .CleanBooks import CleanDataBook
from .GetCoverBooks import GetBookCover

from typing import Iterable , Any

Fields = ['key','title','author_name','subject','isbn','publish_date','publish_place','publisher']
def GetBook(Subjects:list[str],AmountBooks:int) -> Iterable[dict[str,Any]]:
    """
    Function for obtaining clean books from a 
    subject list.

    Parameters
    ----------    
    Subjects : list[str]
        List of subjects
        
    AmountBooks : int
        Amount of books to get

    Returns
    -------
    book : dict
        Representation of a book as a dictionary
    """
    for batch_books in GetBooksData(Subjects,AmountBooks):
        for book in batch_books:
            if all(map(lambda field: book.get(field,False),Fields)) and CleanDataBook(book) and GetBookCover(book):
                yield book

def GetBooksData(Subjects:list[str],AmountBooks:int) -> Iterable[list[tuple[str,str]]]:
    """
    Function for getting data of books from 
    a list of subjects

    Parameters
    ----------
    Subjects : list[str]
        List of subjects
    
    AmountBooks : int
        Amount of books to get

    Returns
    -------
    list[dict]
        Yield a list of books with their data
    """
    for subject in Subjects:
        yield GetTitlesBySubject(subject,AmountBooks)

api_url_search = "https://openlibrary.org/search.json?fields=" + ",".join(Fields)
def GetTitlesBySubject(Subject:str,AmountBooks:int) -> list[dict]:
    """
    Function for getting data of books by subject

    Parameters
    ----------
    Subject : str
        Subject of the books
    
    AmountBooks : int
        Limit of books from which data is extracted

    Returns
    -------
    list[dict]
        List of books with their data
    """
    identification = {
                      "User-Agent":os.getenv("USER_AGENT")
                     }
    parameters_request = {
                        "q":Subject,
                        "lang":"eng",
                        "limit":AmountBooks,
                        "sort":"rating",
                       }
    
    try:
        response_books = requests.get(api_url_search,params=parameters_request,headers=identification)
        response_books.raise_for_status() 
    except requests.exceptions.RequestException as exception:
        titles_subject = []
    else:
        titles_subject = response_books.json()['docs']
    finally:
        return titles_subject