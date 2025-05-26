import requests
from re import fullmatch

API = "http://localhost:8013/recommendations?isbn={isbn}"

def test_GetRecommendations():
    response = requests.get(API.format(isbn='')).json()
    for isbn_code in response:
        assert fullmatch(r'[0-9]{13}',isbn_code)

def test_GetRecommendationsOfBook():
    response = requests.get(API.format(isbn='9780739335871')).json()
    for isbn_code in response:
        assert fullmatch(r'[0-9]{13}',isbn_code)