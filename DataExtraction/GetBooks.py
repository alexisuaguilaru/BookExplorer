import requests
import json

from typing import Iterable

def GetBooksData(Subjects:list[str],AmountBooks:int) -> Iterable[list[tuple[str,str]]]:
    """
        Function for getting data of books from 
        a list of subjects

        -- Subjects : list[str] :: List of subjects

        -- AmountBooks : int :: Amount of books to get

        Yield a list of IDs and titles
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

        Return a list of books with its data
    """
    api_url_subject = f"https://openlibrary.org/subjects/{Subject}.json"
    identification = {
                      "User-Agent":"BookExplorer/School/0.0 (alexis.uaguilaru@gmail.com)"
                     }
    parameters_query = {
                        "details":"false",
                        "limit":AmountBooks
                       }

    response = requests.get(api_url_subject,params=parameters_query,headers=identification)
    data = json.loads(response.text)
    
    return data['works']

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