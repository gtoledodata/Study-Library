url = input("Enter a URL to validate: ")

import re

url_pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/.*)?$'

if re.match(url_pattern, url):
    print("The URL is valid.")
else:
    print("The URL is not valid.")
    
    ## Alternative
    
    if url.startswith("http://") or url.startswith("https://") and url.endswith(".com"):
        print("The URL is valid.")