import requests

import pytest

from test_GetRecommendations import __GetRecommendations

API = "http://localhost:8013/information_book?isbn={isbn}"

def __ValidateInformationOfBook(ISBN_Code):
    response = requests.get(API.format(isbn=ISBN_Code)).json()
    for field in ['author_name','image','isbn','title']:
        yield bool(response[field])

isbn_tests = __GetRecommendations()
@pytest.mark.parametrize('ISBN_Code',isbn_tests)
def test_InformatioBook(ISBN_Code:str):
    invalid_information = list(__ValidateInformationOfBook(ISBN_Code))
    
    assert all(invalid_information) , f"{' '.join(map(str,invalid_information))}"