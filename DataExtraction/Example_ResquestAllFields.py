import requests
from random import choice

if __name__ == "__main__":
    # Setting API
    api_url_search = "https://openlibrary.org/search.json"
    all_fields = {"key","redirects","title","subtitle","alternative_title","alternative_subtitle",
                  "cover_i","ebook_access","edition_count","edition_key","format","by_statement",
                  "publish_date","lccn","ia","oclc","isbn","contributor","publish_place","publisher",
                  "first_sentence","author_key","author_name","author_alternative_name","subject",
                  "person","place","time","has_fulltext","title_suggest","publish_year","language",
                  "number_of_pages_median","ia_count","publisher_facet","author_facet","first_publish_year",
                  "ratings_count","readinglog_count","want_to_read_count","currently_reading_count",
                  "already_read_count","subject_key","person_key","place_key","time_key","lcc",
                  "ddc","lcc_sort","ddc_sort",
                 }
    api_url_search += "?fields=" + ','.join(all_fields)

    # Printing all available fields
    print("Available Field".center(30,'-'))
    print(*all_fields,sep=',\t',end='\n'*2)

    # Setting GET response
    ExamplesSubjects = ['fiction','fantasy','historical_fiction',
                        'horror','humor','literature','magic',
                        'mystery_and_detective_stories','plays',
                        'poetry','romance','science_fiction',
                        'short_stories','thriller','young_adult_fiction']
    identification = {
                      "User-Agent":"BookExplorer/School/0.0 (alexis.uaguilaru@gmail.com)"
                     }
    parameters_request = {
                        "q":choice(ExamplesSubjects),
                        "lang":"eng",
                        "limit":1,
                        "sort":"rating",
                       }
    response = requests.get(api_url_search,params=parameters_request,headers=identification).json()['docs'][0]

    # Printing GET response
    print("Example of GET Response".center(30,'-'))
    print(*response.items(),sep='\n')