## A program to check if a user has access to the office based on the time of day.

time = input("What time is it? (in 24-hour format, e.g., 14) ")

if 8 < int(time) < 18:
    print("You have access to the office.")
else:
    print("You do not have access to the office.") 