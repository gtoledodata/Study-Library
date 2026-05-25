# Program to calculate the total time to finish three activities

A = int(input("Enter the number of hours to finish activity A: "))
B = int(input("Enter the number of hours to finish activity B: "))
C = int(input("Enter the number of hours to finish activity C: "))

total_time = A + B + C

if A < 0 or B < 0 or C < 0:
    print("Invalid input. Please enter non-negative hours.")
else:
    print("The total time to finish all activities is:", total_time, "hours")