word = input("Enter a word: ")

import re 

first_letters = word[0:3]
last_letters = word[-3:]

print("First three letters:", first_letters)
print("Last three letters:", last_letters)