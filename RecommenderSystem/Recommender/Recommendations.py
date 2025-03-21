def GetRecommendations(ISBN:str,BooksCollection:object) -> list[str]:
    if ISBN:
        return list(BooksCollection.find_one({"isbn":ISBN})["similar_books"])
    else:
        return [book["isbn"] for book in BooksCollection.aggregate([{"$sample":{"size":10}},{"$project":{"_id": 0,"isbn":1}}])]