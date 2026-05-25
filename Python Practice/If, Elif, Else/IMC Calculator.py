# Program to calculate the IMC (Body Mass Index)

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")
imc = float(weight) / (float(height) ** 2)

print("Your IMC is: " + str(imc))

if imc < 18.5:
    print("You are underweight")
elif imc < 25:
    print("You are normal weight")
elif imc < 30:
    print("You are overweight")
else:
    print("You are obese")