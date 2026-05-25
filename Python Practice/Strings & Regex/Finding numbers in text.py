prescription = input("Enter the prescription: ")

import re

numbers = re.findall(r'\d+', prescription)

print("Prescription number:", numbers)