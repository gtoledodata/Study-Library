## A program to find all the words in a book title that start with a specific letter entered by the user and print them as a list.

book_title = input("Enter a book title: ")
initial_search_letter = input("Enter the initial letter to search for: ")

import re

matching_words = re.findall(rf'\b{initial_search_letter}[a-z]*\b', book_title, re.IGNORECASE)
print(f'{matching_words} are the book titles that start with "{initial_search_letter}")')