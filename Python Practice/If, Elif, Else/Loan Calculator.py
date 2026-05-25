## A program to calculate the maximum loan amount a person can apply for based on their salary, and check if the requested loan amount is within the limit.

salary = int(input("Enter your salary: "))
max_loan = salary * 0.3
loan_amount = int(input("Enter the loan amount you want to apply for: "))
if loan_amount <= max_loan:
    print("Congratulations! Your loan application has been approved.")
else:
    print("Sorry, your loan application has been denied. The maximum loan amount you can apply for is:", max_loan)
    