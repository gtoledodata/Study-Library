books =[
    {"title": "1984", "inventory": 12},
    {"title": "To Kill a Mockingbird", "inventory": 0},
    {"title": "The Great Gatsby", "inventory": 5},
    {"title": "Pride and Prejudice", "inventory": 2},
    {"title": "Moby Dick", "inventory": 3},
    {"title": "War and Peace", "inventory": 0},
]

for book in books:
    if book["inventory"] == 0:
        continue
    else:
        print(f"{book['title']} is available with {book['inventory']} copies in stock.")
        
        