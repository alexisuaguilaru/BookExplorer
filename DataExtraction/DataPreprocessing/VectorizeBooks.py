from sklearn.feature_extraction.text import TfidfVectorizer

from numpy import ndarray

def GetTermFrequencyMatrix(DataBooks:list[dict]) -> ndarray:
    """
        Function for obtaining TF-IDF matrix 
        given a list of titles and subjects relative 
        to each book.

        -- DataBooks : list[dict] :: MongoDB collection with the data books

        Return TF-IDF matrix 
    """
    TitleSubjectsData_Books = [' '.join(map(str.lower,[book['title']]+book['subject'])) for book in DataBooks]
    TitleSubjectsVectorizer = TfidfVectorizer(stop_words=None)
    return TitleSubjectsVectorizer.fit_transform(TitleSubjectsData_Books)