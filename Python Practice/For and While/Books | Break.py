## A program to search for a specific book in a list and break the loop when found.

books = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick", "War and Peace"]

for book in books:
    if book == "Moby Dick":
        print("Book found! Ending search.")
        break