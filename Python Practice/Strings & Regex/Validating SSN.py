## A program to validate a Social Security Number (SSN) entered by the user, ensuring that it follows the format XXX-XX-XXXX, where X is a digit, using regular expressions.

def check_SSN():
    global SSN
    SSN = input("Enter a Social Security Number (SSN) in the format XXX-XX-XXXX: ")

import re

check_SSN()

while True:
    if re.fullmatch(r'\d{3}-\d{2}-\d{4}', f'{SSN}'):
        print("Valid SSN")
        break
    print("Invalid SSN, please enter in the format XXX-XX-XXXX.")
    check_SSN()