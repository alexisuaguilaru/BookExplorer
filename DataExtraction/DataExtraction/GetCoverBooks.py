import requests
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

api_url_covers = 'https://covers.openlibrary.org/b/isbn/%s-L.jpg?default=false'
def GetBookCover(Book:dict) -> bool:
    """
    Function for adding cover image 
    in a book if it exists and is 
    available    

    Parameters
    ----------
        Book : dict
            Representation of a book

    Returns
    -------
    bool 
        Whether a book has a cover image
    """
    url_cover = api_url_covers%(Book['isbn'])
    response_cover = requests.get(url_cover)

    if response_cover and ValidateDimensionsCover(response_cover.url):
        Book['image'] = url_cover
        return True
    else:
        return False

def ValidateDimensionsCover(URL_Cover:str) -> bool:
    """
    Function for validating dimensions 
    of a image based on when is a 
    no available image

    Parameters
    ----------
    URL_Cover : str
        URL of book's cover image

    Returns
    ------- 
    bool 
        Whether the dimensions of the cover are validate
    """
    with urlopen(URL_Cover) as response:
        img_data = response.read(500000)
        img = Image.open(BytesIO(img_data))
        return img.size[0] != 60