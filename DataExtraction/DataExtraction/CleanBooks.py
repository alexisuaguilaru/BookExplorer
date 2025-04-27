import re

BookFields = ['author_name', 'isbn', 'key', 'publish_date', 'publish_place', 'publisher', 'title', 'subject']
def CleanDataBook(book:dict) -> bool:
    """
        Function for cleaning data of 
        a book, deleting some attributes.

        -- book : dict :: Representation of a book
    """
    for field in BookFields:
        if not CleanFieldBook[field](book):
            return False
    return True

def NotChange(book:dict) -> bool:
    """
        Function for not applying 
        any changes.

        -- book : dict :: Representation of a book
    """
    return True

def Clean_Title(book:dict) -> bool:
    """
        Function for filtering 
        a book by its title 
    """
    title = book['title']
    if 'Works' in title and ('(' in title or '/' in title):
        return False
    return True

filter_subject_pattern = r'[:;=0-9<>_]'
clean_subject_pattern = r'\s*[/\-\(\)\\,\.]+\s*'
def Clean_Subject(book:dict) -> bool:
    """
        Function for filtering 
        elements of subject of 
        a book
    """
    clean_subjects = []
    for subject in book['subject']:
        subject = subject.lower()
        if not re.search(filter_subject_pattern,subject):
            subject_clean = re.sub(clean_subject_pattern,' ',subject)
            clean_subjects.append(subject_clean)
    book['subject'] = clean_subjects
    return True

def Clean_Key(book:dict) -> bool:
    """
        Function for getting the 
        identifier of Open Library.

        -- book : dict :: Representation of a book
    """
    book['key'] = book['key'][7:]
    return True

def Clean_ISBN(book:dict) -> bool:
    """
        Function for getting the 
        ISBN code of a book.

        -- book : dict :: Representation of a book
    """
    for isbn_code in book['isbn']:
        if len(isbn_code) == 13:
            break
    book['isbn'] = isbn_code
    return True

date_type1 = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
date_type2 = r'[A-Za-z]{3} [0-9]{2}, [0-9]{4}'
Month_Number = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def Clean_PublishDate(book:dict) -> bool:
    """
        Function for getting the publish 
        date of a book.
    
        -- book : dict :: Representation of a book
    """
    for date in book['publish_date']:
        if re.fullmatch(date_type1,date) or re.fullmatch(date_type2,date):
            break
    if re.fullmatch(date_type2,date):
        date = '-'.join([date[-4:],Month_Number[date[:3]],date[4:6]])
    book['publish_date'] = date
    return True

def Clean_PublishPlace(book:dict) -> bool:
    """
        Function for getting the publish 
        place of a book.
    
        -- book : dict :: Representation of a book
    """
    for place in book['publish_place']:
        if len(place) > 3:
            break
    book['publish_place'] = place
    return True

def Clean_Publisher(book:dict) -> bool:
    """
        Function for getting the publisher 
        of a book.    

        -- book : dict :: Representation of a book
    """
    for publisher in book['publisher']:
        if len(publisher) != 0:
            break
    book['publisher'] = publisher
    return True

# Dispatch of functions based on field name
CleanFieldBook = {
                    'author_name':NotChange,
                    'title':Clean_Title,
                    'subject':Clean_Subject,
                    'key':Clean_Key,
                    'isbn':Clean_ISBN,
                    'publish_date':Clean_PublishDate, 
                    'publish_place':Clean_PublishPlace, 
                    'publisher':Clean_Publisher,
                  }