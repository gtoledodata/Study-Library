## A program to check if a person's monthly spending is under, on, or over a budget of $3000.

spending = float(input("How much money do you spend each month? "))

if spending < 3000:
    print("You are under budget")
elif spending == 3000:
    print("You are right on budget")
else:
    print("You are over budget")
    