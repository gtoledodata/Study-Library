## Declaring variables

apples = int(input("Type how many apples were sold :"))
bananas = int(input("Type how many bananas were sold :"))

## Checking how may sales were made"

if apples > bananas:
    print("The apples had more sales")
elif apples == bananas:
    print("The sales were tied")
else:
    print("The bananas had more sales")

print("The program is done running")
