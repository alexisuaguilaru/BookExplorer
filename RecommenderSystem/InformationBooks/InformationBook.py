def GetInformationBook(ISBN:str,BooksCollection:object):
    if ISBN:
        return BooksCollection.find_one({"isbn":ISBN},{"_id":0,"isbn":1,"title":1,"author_name":1,"subject":1})
    else:
        return {}