# 1. Create constant collection of numbers, print first size of the collection and elements on even positions

nums = (2, 8, 79, 96, 118, 125)
print(len(nums))
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)

# 2. Create a collection for storing unique book names, add some of them from console and print results

books = {"The Old Man and the Sea", "Brothers Karamazov", "Hamlet"}
input_books = input("Please, enter some book names: ")
books.add(input_books)
print(books)

# 3. Create 2 collections storing company employees,
# get number of employees working in both companies,
# get collection of employees with same name from both of groups,
# input several names and find if they work in one of companies, print results

employees1 = {"Kevin", "Mellisa", "Mike", "William"}
employees2 = {"William", "Sophia", "Mike", "Isabella"}

all_employees = employees1 | employees2
print("The number of employees working in both companies is: ", len(all_employees))

same_name = employees1 & employees2
print(same_name, " - This are the same names from both of groups.")

oneof_companies = []
print("Please, enter the names: ")
for i in range(6): # len(all_employees))
    input_name = input()
    oneof_companies.append(input_name)
    if input_name in all_employees:
        print("He/She works in one of companies.")
    else:
        print("He/She does not work in one of companies.")


# 4. Create 2 collections for storing movies that have been watched by 2 persons,
# get movies that are watched by at least one of them,
# get movies that are watched by 1-st and not watched by 2-nd, print results

person1 = {"Moskva slezam ne verit", "Shinel", "Jestoki romans"}
person2 = {"Spisok Shinglera", "V jazze tol'ko devushki", "Shinel"}

oneof_watcher = person1 | person2
print(oneof_watcher, " - movies that are watched by at least one of them")

first_watcher = person1 - person2
print(first_watcher, " - movies that are watched by 1-st and not watched by 2-nd")

# 5. Input a collection of employee names with their salary,
# calculate average salary in organisation,
# get the employee with highest salary,
# get the employee with lowest salary print results.

employees = {}
for i in range(3):
    print("Please, enter the employee's name: ")
    name = input()
    print("Please, enter the employee's salary: ")
    salary = int(input())
    employees[name] = salary

names = list(employees.keys())
salary = list(employees.values())

average_salary =sum(salary) / len(salary)
print(average_salary)

maximum_salary = max(salary)
i = salary.index(maximum_salary)
print("Employee with highest salary is  -", names[i])

minimum_salary = min(salary)
i = salary.index(minimum_salary)
print("Employee with lowest salary is - ", names[i])

# 6. Calculate multiplication of elements starting from some inputted number up to other inputted number

num1 = int(input("Please, input the first number: "))
num2 = int(input("Please, input the second number: "))
sum = num1*num2
print("Result of multiplication is: ", sum)

# 7. Input 7 numbers, get the numbers from beginning to the number which is less than number on previous position

nums = []
print("Please, enter 7 numbers: ")
for i in range(7):
    num = int(input())
    nums.append(num)
    check_nums = [num for num in nums if num < i]
print(check_nums)

# 8. Define collection of songs, print indexes for songs starting with ‘s’

songs = ("Wind Of Change", "Stand By Me", "Listen To Your Heart", "Sweet Dreams")
for i in range(len(songs)):
    if songs[i].startswith('S'):
        print(i)

# 9 . Define collection of prices, calculate their sum until meeting negative price

prices = [10,50,100,40,-50,-100]
sum=0
for i in prices:
    sum+=i
    if i<0:
        break
    print(sum)

# 10. Calculate multiplication of numbers from 0 to inputted value and print it

list_num = int(input("Please, enter a number: "))
result = 1
for i in range(list_num):
    if i == 0:
        continue
    result *= i
print(result)

# 11. Input collection of numbers, find last number which square root is less than 26, print it

import math
numbers = []
print("Please, enter 3 numbers: ")
for i in range(3):
    input_number = int(input())
    numbers.append(input_number)
for number in numbers:
    if math.sqrt(number) < 26:
        print(number)
        break