## Lists and Tuples

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, "text", 3.14, True, [1, 2, 3]]

# in tuples elements can't be changed, but in lists they can be changed

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (1, "text", 3.14, True, [1, 2, 3])

# Print elements 

print(list_1[0]) # 1
print(tuple_2[1]) # text
print(tuple_1[2:4]) # (3, 4)

# Check if elements are present

print(20 in list_1) # False
print(3 in tuple_1) # True

# Manipulating elements in lists

list_1.append(6) # adds an element to the end of the list
list_1.insert(2, 10) # adds an element at a specific index in the list
list_1.remove(3) # removes the first occurrence of an element from the list
list_1.reverse() # reverses the order of the elements in the list
list_1.sort() # sorts the elements in the list in ascending order
list_1.pop() # removes and returns the last element of the list

# Manipulating elements in tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

new_tuple = tuple1 + tuple2 # concatenates two tuples
print(new_tuple) # (1, 2, 3, 4, 5, 6)

for element in tuple1:
    print(element) # 1, 2, 3

tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = tuple # unpacking a tuple into individual variables
print(a) # 1

## Example code

chores = ["cleaning", "cooking", "laundry", "grocery shopping"]

chores.append("dishes") # adds "dishes" to the end of the list

chores.remove("laundry") # removes "laundry" from the list

for chore in chores:
    print(chore) # prints each chore in the list
    
    
## Example code 2

city1 = ("New York", -40.7128, -74.0060)
city2 = ("Los Angeles", 34.0522, -118.2437)
city3 = ("Chicago", 41.8781, -87.6298)

cities = [city1, city2, city3]

for city in cities:
    name, latitude, longitude = city
    print(f"{name}: Latitude {latitude}, Longitude {longitude}")
    
    
