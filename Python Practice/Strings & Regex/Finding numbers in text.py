##  A program to find all the numbers in a prescription text entered by the user and print them as a list.

prescription = input("Enter the prescription: ")

import re

numbers = re.findall(r'\d+', prescription)

print("Prescription number:", numbers)