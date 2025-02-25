import requests

from typing import Iterable

def GetBooksData(Subjects:list[str],AmountBooks:int) -> Iterable[list[tuple[str,str]]]:
    """
        Function for getting data of books from 
        a list of subjects

        -- Subjects : list[str] :: List of subjects

        -- AmountBooks : int :: Amount of books to get

        Yield a list of books with their data
    """
    for subject in Subjects:
        books = GetTitlesBySubject(subject,AmountBooks)
        yield ExtractDataBooks(books)

def GetTitlesBySubject(Subject:str,AmountBooks:int) -> list[dict]:
    """
        Function for getting data of books by subject

        -- Subject : str :: Subject of the books

        -- AmountBooks : int :: Limit of books from which 
        data is extracted

        Return a list of books with their data
    """
    api_url_search = "https://openlibrary.org/search.json?fields=key,title,author_name,subject,isbn,publish_date,publish_place,publisher"
    identification = {
                      "User-Agent":"BookExplorer/School/0.0 (alexis.uaguilaru@gmail.com)"
                     }
    parameters_request = {
                        "q":Subject,
                        "lang":"eng",
                        "limit":AmountBooks,
                        "sort":"rating",
                       }

    response = requests.get(api_url_search,params=parameters_request,headers=identification)
    return response.json()['docs']

def ExtractDataBooks(Books:list[dict]) -> list[tuple[str,str]]:
    """
        Function for extracting essential data from books    
    
        -- Books : list[dict] :: List of books data 

        Return a list of IDs and titles
    """
    ExtractedData = []

    for book in Books:
        ExtractedData.append((book['key'][7:],book['title']))
    
    return ExtractedData