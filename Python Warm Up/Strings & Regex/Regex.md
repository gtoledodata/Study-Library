## Regex Instructions

.   any character, except new line
\d  any digit (0-9)
\D  Any character that is not a difit
\w  Any alphanumeric character
\W  Any non alphanumeric character
\s  Any blank space
\S  Any non blank space

\b word limit \b

[abc]
[ˆabc] Not "a", "b", "c"
[a-z] Any from a to z
[A-Z] Any from a to z (Uppercase)
[0-9] Any 0 to 9 digit
[a-zA-Z] Any letter (upper or lower case)

* 0+ instances
+ 1+ instances
? 0 or 1 instance
{n} n instances
{n,} n+ instances
{n,m} between n - m instances
 
 ## Phone Number Regex:

 (11) 94559-0272

 \(\d{2}\)\s\d{4-500}-\d{4}

 ## DOB: DD/MM/AAAA

 \b\d{2}/\d{2}/\d{4}\b

 ## Re Module

 import re

 -------------

 re.search(r"\d+", "There are 1234 students") -> 1234

 re.match(r"abc", "abcdef") -> 1 match

 re.findall(r"\d+", "I have 3 cats and 2 dogs") -> ["3", "2"]

 re.sub(r"\d", "#", "Meu número é 1234") -> My number is ####