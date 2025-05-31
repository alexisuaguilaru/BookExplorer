import requests
from re import fullmatch

import pytest

from typing import Iterable

API = "http://localhost:8013/recommendations?isbn={isbn}"

def __GetRecommendations(ISBN_Code:str='') -> Iterable[str]:
    response = requests.get(API.format(isbn=ISBN_Code)).json()
    for isbn_code in response:
        yield isbn_code

def __ValidateISBNCode(ISBN_Code:str) -> bool:
    return fullmatch(r'[0-9]{13}',ISBN_Code)

isbn_code = list(__GetRecommendations())[:5]
isbn_tests = ['','',*isbn_code]
@pytest.mark.parametrize('ISBN_Code',isbn_tests)
def test_Recommendations(ISBN_Code:str):
    invalid_isbn_codes = []
    for isbn_code in __GetRecommendations(ISBN_Code):
        if not __ValidateISBNCode(isbn_code):
            invalid_isbn_codes.append(isbn_code)
    
    assert not invalid_isbn_codes , f"{' '.join(invalid_isbn_codes)}"