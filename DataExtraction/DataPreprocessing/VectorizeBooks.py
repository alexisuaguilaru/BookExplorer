from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np

def GetTermFrequencyMatrix(DataBooks:list[dict]) -> np.ndarray:
    """
    Function for obtaining TF-IDF matrix 
    given a list of titles and subjects relative 
    to each book.

    Parameters
    ----------
    DataBooks : list[dict]
        MongoDB collection with the data books

    Returns
    -------
    TitleSubjectsVectorized : np.ndarray
        TF-IDF matrix 
    """
    TitleSubjectsData_Books = [' '.join(map(str.lower,[book['title']]+book['subject'])) for book in DataBooks]
    TitleSubjectsVectorizer = TfidfVectorizer(stop_words=None)
    return TitleSubjectsVectorizer.fit_transform(TitleSubjectsData_Books)