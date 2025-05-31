from typing import Any

def GetInformationBook(ISBN:str,BooksCollection:object) -> dict[str,Any] | dict:
    """
    Function for getting essential information 
    of a given ISBN code

    Parameters
    ----------
    ISBN : str
        Book's ISBN code which its information is gathered

    BooksCollection : object
        MongoDB collection where the books belong

    Returns
    -------
    dict 
        A dictionary with the information of a book or a 
        empty one if not exist the queried book
    """
    if ISBN:
        return BooksCollection.find_one({"isbn":ISBN},{"_id":0,"isbn":1,"title":1,"author_name":1,"subject":1,"image":1})
    else:
        return {}