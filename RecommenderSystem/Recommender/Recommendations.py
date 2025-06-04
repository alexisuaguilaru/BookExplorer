def GetRecommendations(ISBN:str,BooksCollection:object) -> list[str]:
    """
    Function for getting recommendations of a book

    Parameters
    ----------
    ISBN : str
        Book's ISBN code which its information is gathered

    BooksCollection : object
        MongoDB collection where the books belong

    Returns
    -------
    list[str]
        Returns a list of ISBN books recommendations
    """
    if ISBN:
        return list(BooksCollection.find_one({"isbn":ISBN})["similar_books"])
    else:
        return [book["isbn"] for book in BooksCollection.aggregate([{"$sample":{"size":10}},{"$project":{"_id": 0,"isbn":1}}])]