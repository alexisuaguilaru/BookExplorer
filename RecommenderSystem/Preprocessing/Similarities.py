from numpy import ndarray

def InsertSimilarBooks(DataBooks:list[dict],BooksSimilarity:ndarray,BooksCollection:object) -> None:
    """
        Function for inserting similar books using cosine 
        similarity at each book.

        -- DataBooks : list[dict] :: MongoDB collection with the data books 
        -- BooksSimilarity : ndarray :: Matrix of book cosine similarities
        -- BooksCollection : object :: MongoDB collection where the books belong
    """
    for index , book in enumerate(DataBooks):
        similarity_scores = list(enumerate(BooksSimilarity[index]))
        top_books = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:11]
    
        BooksCollection.update_one(
            {'isbn': book['isbn']},
            {'$set': {"similar_books": [DataBooks[j[0]]['isbn'] for j in top_books]}}
        )