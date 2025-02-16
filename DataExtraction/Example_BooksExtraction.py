from GetBooks import GetBooksData

from random import sample , randint

if __name__ == '__main__':
    ExamplesSubjects = ['fiction','fantasy','historical_fiction',
                        'horror','humor','literature','magic',
                        'mystery_and_detective_stories','plays',
                        'poetry','romance','science_fiction',
                        'short_stories','thriller','young_adult_fiction']
    
    subjects = sample(ExamplesSubjects,2)
    AmountBooks = randint(2,50)

    for subject , data_books in zip(subjects,GetBooksData(subjects,AmountBooks)):
        print(f'\n{subject.upper().center(40,'-')}\n')
        for id , title in data_books:
            print(f'{id}\t{title}')