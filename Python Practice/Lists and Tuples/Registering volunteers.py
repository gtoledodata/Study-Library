##A program to register volunteers

volunteers = []

while True:
    name = input("Enter volunteer's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    volunteers.append(name)

print("Registered volunteers:")
for volunteer in volunteers:
    print(f"- {volunteer}")