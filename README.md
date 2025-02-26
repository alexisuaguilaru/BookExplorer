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

## Methodology
The Extreme Programming (XP) methodology was used for this project, with development cycles of 1 to 2 weeks.

## Usage Instructions
First it is necessary to clone this repository:
```bash
git clone https://github.com/alexisuaguilaru/BookExplorer.git
```
Next, build the container image using Docker and then run it:
```bash
docker build --tag book_explorer:0.1 .
```
Finally, for executing the book extraction examples, execute the following commands:
```bash
docker run --rm book_explorer:0.1 python DataExtraction/Example_BooksExtraction.py
docker run --rm book_explorer:0.1 python DataExtraction/Example_RequestAllFields.py
```