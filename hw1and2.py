import math

# 1. Write program for calculating (a+b)^2 for some a and b
a = 3
b = 4
c = (a+b)**2
print(c)

# 2. Write following program: calculate how much money you should pay for 1500$ bank loan if annual percentage is 16%

loan = 1500
sum = loan * 0.16
payment = loan + sum * 0.16
print(payment)

# 3. Write program for calculating the hypotenuse along two legs in a right-angled triangle

from math import hypot

p = 3
b = 4
print("Hypotenuse is:", hypot(p, b))

#4. Greet user with his name inputed from console

print("Please, enter your Name: ")
username = input()
print("Hello, " + username)

# 5. Create 2 modules:
# 1. containing data about student;
# 2. using data from first module

import hw1and2_ex5_module
print(hw1and2_ex5_module.student_info)

# 6. Write a square root calculator that performs for some inputted value

x = int(input("Please, enter a number: "))
print(math.sqrt(x))

# 7. Write a program that guesses user age randomly

import random

age = (random.randint(18,38))
print("Your age is ", age)

# 8. Write a program containing 3 modules:
# 1. calculating power of number (number and power are inputted from console),
# 2. calculating remainder of some number divided to other number (inputted from console),
# 3. performing operation from first and second module

import hw1_module1
print(hw1_module1.result)

import hw1_module2
print(hw1_module2.remainder_result)

# 9. Write some comments to your code

# One-line comment
# Calculating square root and print  - print(math.sqrt(36))

# Multiline- comments
'''
This is a multiline 
comment
'''

"""
This is another  
comments
"""