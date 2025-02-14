import requests
import json

def GetTitlesBySubject(Subject:str) -> list[dict]:
    """
        Function to get data from books by subject

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