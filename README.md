# BookExplorer

## Abstract
Recommender system based on user preferences to explore new titles.

## Author and Contact
Alexis Aguilar [Student of Bachelor's Degree in "Tecnologías para la Información en Ciencias" at Universidad Nacional Autónoma de México [UNAM](https://www.unam.mx/)]: alexis.uaguilaru@gmail.com 

## License
Project under [MIT License](LICENSE)

## Introduction
As there is an enormous amount of titles, it becomes overwhelming how to find new books that fit a preference or previously read books. Therefore, this project, whose product is to create a service, aims to create a solution to explore new titles based on the user's preferences and previous books.

For capturing these preferences and previous readings (titles read), what is done is to show the user three different books to choose from, avoiding overloading the user with information and details of the books.

## General Aim
Develop a book recommendation system that is intuitive and simple to use for the user, with which suggestions are adjusted based on their preferences, specifically, by the books whose covers and titles caught their attention. In order to create an alternative solution to the question of what to read by simulating going to a bookstore and choosing a book only by reading its title and seeing its cover.

## Methodology
The Extreme Programming (XP) methodology was used for this project, with development cycles of 1 to 2 weeks.

The progress tracking of this methodology is found in the closed issues and pull requests labeled with the code of each activity and cycle found in the project's [Jira]().

## Installation and Usage Instructions
First it is necessary to clone this repository:
```bash
git clone https://github.com/alexisuaguilaru/BookExplorer.git
```
Next, build and run the multi-container image using Docker Compose:
```bash
docker-compose -p books-explorer --file Docker-Compose.yml --env-file .env_example up -d --build
```
And finally, to view the web interface just open the following link:
```bash
http://localhost:5000
```
### Examples
Because the Python container related to the backend stops, it is necessary to first start it to run the exemplars.
* Example to See all Available Fields (Categories)
    ```bash
    docker-compose -p books-explorer start PythonBackend
    docker-compose -p books-explorer exec PythonBackend python -m DataProcessing.Examples.Example_RequestAllFields
    ```

* Example of Books Extraction
    ```bash
    docker-compose -p books-explorer start PythonBackend
    docker-compose -p books-explorer exec PythonBackend python -m DataProcessing.Examples.Example_BooksExtraction
    ```

* Example of Query of Three Random Books
    ```bash
    docker-compose -p books-explorer start PythonBackend
    docker-compose -p books-explorer exec --env .env_example PythonBackend python DataProcessing/Examples/Example_Random3Books.py
    ```