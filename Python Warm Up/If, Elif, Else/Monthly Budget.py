spending = float(input("How much money do you spend each month? "))

if spending < 3000:
    print("You are under budget")
elif spending == 3000:
    print("You are right on budget")
else:
    print("You are over budget")
    