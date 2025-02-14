from time import sleep
import requests
import json

def GetBooksData(Subjects:list[str]) -> list[tuple[str,str]]:
    """
        Function for getting data of books from 
        a list of subjects

        -- Subjects : list[str] :: List of subjects 

        Return a list of titles and IDs
    """
    for subject in Subjects:
        books = GetTitlesBySubject(subject)
        yield ExtractDataBooks(books)
        sleep(1.5)

def GetTitlesBySubject(Subject:str) -> list[dict]:
    """
        Function for getting data of books by subject

        -- Subject : str :: Subject of the books

        Return a list of books with its data
    """
    api_url_subject = f"https://openlibrary.org/subjects/{Subject}.json"
    identification = {
                      "User-Agent":"BookExplorer/School/0.0 (alexis.uaguilaru@gmail.com)"
                     }
    parameters_query = {
                        "details":"false"
                       }

    response = requests.get(api_url_subject,params=parameters_query,headers=identification)
    data = json.loads(response.text)
    
    return data['works']