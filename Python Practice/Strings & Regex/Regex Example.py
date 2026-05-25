## A program to find an email address in a given text using regular expressions and print it if found.

import re

text = "Get in touch with us at test@email.com"

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.search(email_pattern, text)

if result:
    print("Email found:", result.group())
else:
    print("No email found.")
    
## Website: regex101.com