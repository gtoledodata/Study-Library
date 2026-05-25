## A program to validate a name entered by the user, ensuring that it starts with a capital letter and only contains letters, using regular expressions.

name = input("Enter a name: ")

import re

if re.fullmatch(r'[A-Z][a-z]*', name):
    print("Valid name")
else:
    print("Invalid name, start with a capital letter and only contain letters.")