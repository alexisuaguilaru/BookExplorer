# BookExplorer

## Abstract
Recommendation system based on user preferences to explore new titles using similarities between books.

## Author and Contact
Alexis Aguilar [Student of Bachelor's Degree in "Tecnologías para la Información en Ciencias" at Universidad Nacional Autónoma de México [UNAM](https://www.unam.mx/)]: alexis.uaguilaru@gmail.com

Project developed for the subject “Distributed Computing” for the class taught in semester 2025-2.

## License
Project under [MIT License](LICENSE)

## Introduction
As there is an enormous amount of titles, it becomes overwhelming how to find new books that fit a preference or previously read books. Therefore, this project, whose product is to create a service, aims to create a solution to explore new titles based on the user's preferences and previous books.

For capturing these preferences and previous readings (titles read), what is done is to show the user three different books to choose from, avoiding overloading the user with information and details of the books.

## Justification
The development of this project solves a constant problem among readers, which is the question of which book to read. Therefore, giving different book options to the users could facilitate the resolution of the next reading for each reader. Because of the latter, it becomes the main reason for the development of this solution making use of the reader's own preferences.

## General Aim
Develop a book recommendation system that is intuitive and simple to use for the user, with which suggestions are adjusted based on their preferences, specifically, by the books whose covers and titles caught their attention. In order to create an alternative solution to the question of what to read by simulating going to a bookstore and choosing a book only by reading its title and seeing its cover.

## Particular Aims
- Making book recommendations that allow users to explore new genres based on their selections and preferences.
- Making use of technologies such as containers (Docker), APIs and Machine Learning to develop the book recommender.
- Service the recommender system through a web interface with the user, deployed on a server hosted in the cloud.

## Methodology
The Extreme Programming (XP) methodology was used for this project, with development cycles of 1 to 2 weeks. The progress tracking of this methodology is found in the closed issues and pull requests labeled with the code of each activity and cycle found in the project's [Jira](https://alexisuaguilaru.atlassian.net/jira/software/projects/SCRUM/boards/1/timeline?epic=COMPLETE6M&selectedIssue=SCRUM-40&shared=&atlOrigin=eyJpIjoiNGZiYmNkZTZmMzA0NDVkMTgzZTZjNGU5ZjkzZWZhNzAiLCJwIjoiaiJ9).

First, the books obtained through the [OpenLibrary API](https://openlibrary.org/developers) were processed, from which only the fields of interest for the project (author, title, ISBN, genres, place and date of publication, publisher) were stored. The processed books were stored in MongoDB, to later represent the genres of each book in a numerical vector, which were used to determine the similarity between books; the latter being the basis of the books that are recommended through this service.

For performing the interaction between the web interface (client) and the recommender system (server), Flask was used to provide the communication service between both parts. Finally, the web interface was implemented in Flask to preserve greater security and isolation with the backend of the web service.

## Installation and Usage Instructions
First it is necessary to clone this repository:
```bash
git clone https://github.com/alexisuaguilaru/BookExplorer.git
```
Next, build and run the multi-container for backend (database, interface-API) and frontend (web interface) using Docker Compose:
```bash
docker-compose -p books-explorer --file Compose-Backend.yml --env-file .env_example up -d --build
docker-compose -p books-explorer --file Compose-Frontend.yml --env-file .env_example up -d --build
```
And finally, for interacting with the web interface go to:
```bash
http://127.0.0.1:5000
```
For stopping the service, use this command:
```bash
docker-compose -p books-explorer down
```
### Examples
Because the Python container related to the backend stops, it is necessary to first start it to run the exemplars.
* Example to See all Available Fields (Categories)
    ```bash
    docker-compose -p books-explorer start DataExtraction
    docker-compose -p books-explorer exec DataExtraction python -m DataProcessing.Examples.Example_RequestAllFields
    ```

* Example of Books Extraction
    ```bash
    docker-compose -p books-explorer start DataExtraction
    docker-compose -p books-explorer exec DataExtraction python -m DataProcessing.Examples.Example_BooksExtraction
    ```

* Example of Query of Three Random Books
    ```bash
    docker-compose -p books-explorer start DataExtraction
    docker-compose -p books-explorer exec --env .env_example DataExtraction python DataProcessing/Examples/Example_Random3Books.py
    ```

* Example of Random Recommendations using Recommender System API:
    ```bash
    http://127.0.0.1:8013/recommendations
    ```
  
* Example of Recommendations based on a Book using Recommender System API:
    ```bash
    http://127.0.0.1:8013/recommendations?isbn=9780905712604
    ```

* Example of Get Information of a Book using Recommender System API:
    ```
    http://127.0.0.1:8013/information_book?isbn=9781432896935
    ```

## Technologies
* APIs
* Python
  * Flask
  * Scikit Learn
* MongoDB
* Docker
  * Docker Compose
* AWS
  * EC2