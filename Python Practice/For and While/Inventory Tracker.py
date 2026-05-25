## A program to track inventory levels and simulate sales until the inventory is depleted.
Inventory = 5

while Inventory > 0:
    print("Sale made! Inventory:", Inventory)
    Inventory -= 1
    if Inventory == 0:
        print("Inventory is empty! Ending sales.")
    