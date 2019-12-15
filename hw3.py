import math
# 1. Input 3 floats from console, calculate their sum and print result
number1 = float(input("Please, enter first float number: "))
number2 = float(input("Please, enter second float number: "))
number3 = float(input("Please, enter third float number: "))
sum = number1 + number2 + number3
print(sum)

# 2. Input 2 integers from console, calculate their division as integer and print the result

number1 = int(input("Please, enter first number: "))
number2 = int(input("Please, enter second number: "))
print(number1//number2)

# 3. Input 2 numbers from console and check if both of them are positive

num1 = int(input("Plese, eter first number: "))
num2 = int(input("Plese, eter second number: "))
print("Both of this numbers are positive.") if num1 > 0 and num2 > 0 else print("One or two numbers are not positive.")

# 4. Ask user to input number from console and check if it contains any symbols

print("Please, input a number: ")
input_number = int(input())
check_number = print("Yes") if input_number == 5 else print("No")

# 5. Read an integer from console and if it is positive calculate it’s square root

input_number = int(input("Please, input a number: "))
print(math.sqrt(input_number)) if input_number > 0 else print("It is not positive number.")

# 6. Input 2 number from console (1-st is integer, 2-nd float), calculate their sum and concatenation

num_int = int(input("Please, enter an integer number: "))
num_float = float(input("Please, enter a float number: "))
sum = num_int + num_float
print(sum)
concatenate = str(num_int) + str(num_float)
print(concatenate)

# 7. Generate a random number from 1 to 100 and check if the number is greater than 15 and less than 36

from random import *
random_num = randint(1, 100)
print(random_num)
print("The number is greater than 15 and less than 36.") if random_num > 15 and random_num < 36 else print("Other number")

# 8. Read an integer from console and calculate it’s factorial if it’s positive and less than 100

fact_number = int(input("Please, enter a number: "))
print(math.factorial(fact_number)) if fact_number > 0 < 100 else print ("It is not positive number.")

# 9. Create 2 modules:
# 1. stores some attributes about a room (color, number, etc.);
# 2. makes some operations on attributes of first module

room_color = "White"
room_number = 15
room_square = 100
balcony_square = 10
