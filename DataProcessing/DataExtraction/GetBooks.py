import requests
import os

from DataPreprocessing import CleanDataBook

from typing import Iterable , Any

Fields = ['key','title','author_name','subject','isbn','publish_date','publish_place','publisher']
def GetBook(Subjects:list[str],AmountBooks:int) -> Iterable[dict[str,Any]]:
    """
        Function for obtaining clean books from a 
        subject list.
        
        -- Subjects : list[str] :: List of subjects

        -- AmountBooks : int :: Amount of books to get

        Yield a book 
    """
    for batch_books in GetBooksData(Subjects,AmountBooks):
        for book in batch_books:
            if all(map(lambda field: book.get(field,False),Fields)):
                CleanDataBook(book)
                yield book

def GetBooksData(Subjects:list[str],AmountBooks:int) -> Iterable[list[tuple[str,str]]]:
    """
        Function for getting data of books from 
        a list of subjects

        -- Subjects : list[str] :: List of subjects

        -- AmountBooks : int :: Amount of books to get

        Yield a list of books with their data
    """
    for subject in Subjects:
        yield GetTitlesBySubject(subject,AmountBooks)

api_url_search = "https://openlibrary.org/search.json?fields=" + ",".join(Fields)
def GetTitlesBySubject(Subject:str,AmountBooks:int) -> list[dict]:
    """
        Function for getting data of books by subject

        -- Subject : str :: Subject of the books

        -- AmountBooks : int :: Limit of books from which 
        data is extracted

        Return a list of books with their data
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

    response = requests.get(api_url_search,params=parameters_request,headers=identification)

    if response.status_code == 200:
        return response.json()['docs']
    else:
        return []