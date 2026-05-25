#Program to check if the server temperature is above the limit

server_temp = int(input("Enter the current server temperature: "))

if server_temp > 25:
    print("It's hotter than the limit")
else:
    print("The server temperature is within the limit") 
    