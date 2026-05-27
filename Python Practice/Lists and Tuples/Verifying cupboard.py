## Verifying cupboard contents

item_request = input("Enter the item you want to check: ")
cupboard = ["plates", "cups", "forks", "spoons", "knives"]

if item_request in cupboard:
    print(f"{item_request} is in the cupboard.")
else:
    print(f"{item_request} is not in the cupboard.")
    