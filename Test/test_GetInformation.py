import requests

API = "http://localhost:8013/information_book?isbn={isbn}"

def test_GetInformationOfBook():
    response = requests.get(API.format(isbn='9780739335871')).json()
    assert True
    for field in ['author_name','image','isbn','title']:
        assert response[field]