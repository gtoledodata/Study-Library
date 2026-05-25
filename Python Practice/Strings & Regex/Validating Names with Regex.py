name = input("Enter a name: ")

import re

if re.fullmatch(r'[A-Z][a-z]*', name):
    print("Valid name")
else:
    print("Invalid name, start with a capital letter and only contain letters.")