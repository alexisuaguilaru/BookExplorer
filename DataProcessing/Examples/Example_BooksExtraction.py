from DataProcessing import GetBook

from random import sample , randint

if __name__ == '__main__':
    # Setting random variables for request
    ExamplesSubjects = ['fiction','fantasy','historical_fiction',
                        'horror','humor','literature','magic',
                        'mystery_and_detective_stories','plays',
                        'poetry','romance','science_fiction',
                        'short_stories','thriller','young_adult_fiction']
    subjects = sample(ExamplesSubjects,2)
    AmountBooks = randint(2,15)
    ExampleFields = ["key","title","author_name","subject","isbn","publish_date","publish_place","publisher"]

    # Getting books data 
    for subject in subjects:
        print(f'\n{subject.upper().center(40,'-')}\n')
        fields = sample(ExampleFields,2)
        print(('-'*10).join(fields).center(40,'-'))
        for index_book ,data_book in enumerate(GetBook([subject],AmountBooks)):
            print(f'{index_book}\t{data_book[fields[0]]}\t\t{data_book[fields[1]]}')