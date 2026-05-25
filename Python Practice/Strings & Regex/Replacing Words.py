text = input("Enter text to be revised: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")

import re

revised_text = re.sub(rf'\b{word_to_replace}\b', replacement_word, text)
print("Revised text:", revised_text)