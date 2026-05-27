## Combining Inventories

inventory1 = tuple(input("Enter the first inventory (comma-separated): ").split(", "))
inventory2 = tuple(input("Enter the second inventory (comma-separated): ").split(", "))

combined_inventory = inventory1 + inventory2
print("Combined Inventory:", combined_inventory)