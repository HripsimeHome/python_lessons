# 1. Input 3 collections of numbers, calculate how many numbers are greater than 10 for first,
# how many numbers are greater than 20 for second and how many numbers are greater than 30 for third collection
# (implement version without functions and version with functions)

# Version without function:

first_collection = []
second_collection = []
third_collection = []

count1 = 0
count2 = 0
count3 = 0

print ("Please, input 3 numbers for the first collection: ")
for i in range(3):
    number1 = int(input())
    first_collection.append(number1)
    if number1 > 10:
        count1 +=1

print ("Please, input 3 numbers for the second collection: ")
for i in range(3):
    number2 = int(input())
    second_collection.append(number2)
    if number2 > 20:
        count2 += 1

print ("Please, input 3 numbers for the third collection: ")
for i in range(3):
    number3 = int(input())
    third_collection.append(number3)
    if number3 > 30:
        count3 += 1
print("Greater than 10: ", count1)
print("Greater than 20: ", count2)
print("Greater than 30: ", count3)

# Version with functions

first_collection = []
second_collection = []
third_collection = []

def greater_10(numbers):
    count = 0
    print("Please, enter 3 numbers to the first collection: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        if number > 10:
            count += 1
    return count

def greater_20(numbers):
    count = 0
    print("Please, enter 3 numbers to the second collection: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        if number > 20:
            count += 1
    return count

def greater_30(numbers):
    count = 0
    print("Please, enter 3 numbers to the third collection: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        if number > 30:
            count += 1
    return count
print("Grater than 10:", greater_10(first_collection))
print("Grater than 20:", greater_20(second_collection))
print("Grater than 30:", greater_30(third_collection))


# 2. Input a collection of numbers, calculate how many numbers are positive and dividable by 6 (create a function),
# generate a new collection of odd numbers (create a function), print results

numbers_list = []
def check_numbers(numbers):
    count = 0
    print("Please, enter 3 numbers to check positive numbers: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        if number > 0 and number % 6 == 0:
            count +=1
    return count
print("Positive and dividable by 6: ", check_numbers(numbers_list))


# generate a new collection of odd numbers
main_list = [1, 3, 5, 8, 56, 79]
def odd_numbers(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 1:
            new_list.append(number)
    return new_list
print(odd_numbers(main_list))


# 3. Define a collection of company employees (full name(‘Jack Smith’), position),
# calculate how many people with name ‘John’ work in company (create a function),
# calculate how many people have ‘Engineer’ position (create a function), print results

# calculate how many people with name ‘John’ work in company

employee = {
    "Jack Smith"  : "Engineer",
    "John Taylor" : "Developer",
    "David Scott" : "Engineer",
    "John Parker" : "Engineer",
    "Denis Smith" : "Manager"
}
def name_calculate(position, name="John"):
    count = 0
    for i in position.keys():
        if i[:4] == name:
            count += 1
    return count
print("There are", name_calculate(employee), "people with name John.")


# calculate how many people have ‘Engineer’ position
employee = {
    "Jack Smith"  : "Engineer",
    "John Taylor" : "Developer",
    "David Scott" : "Engineer",
    "John Parker" : "Engineer",
    "Denis Smith" : "Manager"
}
def position_calculate(name, position):
    count = 0
    for i in name.values():
       if i == position:
         count += 1
    return count
print("There are", position_calculate(employee, "Engineer"), "Engineers.")


# 4. Create a collection of hotel rooms (room number, state (booked or not), type (econom, business, lux)),
# calculate how many rooms are booked (create a function), calculate how many numbers of different types by default lux numbers are free (create a function),
# generate a collection of econom numbers, print results

rooms = {'room1': {'number': '1', 'state': 'booked', 'type': 'econom'},
         'room2': {'number': '2', 'state': 'booked', 'type': 'econom'},
         'room3': {'number': '3', 'state': 'not_booked', 'type': 'econom'},
         'room4': {'number': '4', 'state': 'booked', 'type': 'business'},
         'room5': {'number': '5', 'state': 'not_booked', 'type': 'business'},
         'room6': {'number': '6', 'state': 'booked', 'type': 'lux'},
         'room7': {'number': '7', 'state': 'not_booked', 'type': 'lux'}}

# calculate how many rooms are booked
def booked(rooms):
    count = 0
    for room in rooms:
        if rooms[room]['state'] == 'booked':
            count += 1
    return count
print("There are", booked(rooms), "booked rooms")


# calculate how many numbers of different types by default lux numbers are free
def free_rooms(rooms, free='not_booked'):
    count = 0
    for room in rooms:
        if rooms[room]['state'] == free:
            count +=1
    return count
print(free_rooms(rooms))


# generate a collection of econom numbers
def econom_rooms(rooms):
    econom_list = []
    for room in rooms:
        if rooms[room]['type'] == 'econom':
            econom_list.append(room)
    return econom_list
print(econom_rooms(rooms))


# 5. Create a collection of company names, generate a collection of company names ending with ‘s’ (create a function),
# generate a collection of company names containing different symbols combination by default double ‘o’ (create a function), print results


# generate a collection of company names ending with ‘s’
companies = ['Synopsys', 'Microsoft', 'Apple', "HelpSystems", "iNexxus", "Google"]
def check_s(names):
    company_names = []
    for name in names:
        if name.endswith(("s")):
            company_names.append(name)
    return company_names
print(check_s(companies))

# generate a collection of company names containing different symbols combination by default double ‘o’
def check_o(names, double_o="oo"):
    company_names = []
    for name in names:
        if name.count(double_o):
            company_names.append(name)
    return company_names
print(check_o(companies))


# 6. Create a calculator with different functions:
# 1) input numbers (one or more);
# 2) calculate different power for inputted numbers;
# 3) calculate how many numbers are greater than some specific number;
# 4) calculate how many numbers are even;
# 5) get number which power 3 is greater than 100


# 1) input numbers (one or more);
# 2) calculate different power for inputted numbers;
numbers_list = []
def number_power(numbers):
    print("Please, enter 3 numbers to calculate different power: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        print (number**2, number**3)
number_power(numbers_list)

# 3) calculate how many numbers are greater than some specific number;
numbers_list = []
def greater_50(numbers):
    count = 0
    print("Please, enter 3 numbers: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        if number > 50:
            count +=1
    return count
print(greater_50(numbers_list))

# 4) calculate how many numbers are even;
numbers_list = []
def even_numbers(numbers):
    count = 0
    print("Please, enter 3 numbers: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        if number % 2 == 0:
            count +=1
    return count
print(even_numbers(numbers_list))

# 5) get number which power 3 is greater than 100
numbers_list = []
def power_greater_100(numbers):
    print("Please, enter 3 numbers to check pow: ")
    for i in range(3):
        input_number = int(input())
        numbers.append(input_number)
    for number in numbers:
        if number **3 > 100:
            print (number)
power_greater_100(numbers_list)

