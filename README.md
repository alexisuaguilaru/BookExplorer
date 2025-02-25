# BookExplorer

## Abstract
System based on user preferences to recommend new books.

## Author and Contact
Alexis Aguilar [Student of Bachelor's Degree in "Tecnologías para la Información en Ciencias" at Universidad Nacional Autónoma de México [UNAM](https://www.unam.mx/)]: alexis.uaguilaru@gmail.com 

## License
Project under [MIT License](LICENSE)

## Introduction
This project aims to create a solution to explore new titles based on the user's preferences, tastes and previously read books. 

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