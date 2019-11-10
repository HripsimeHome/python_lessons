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

employees1 = {"Kevin", "Mellisa", "Jonathan", "William"}
employees2 = {"William", "Sophia", "Mike", "Isabella"}

same_name = employees1 & employees2
print(same_name, " - This is the same name from both of groups.")

all_employees = employees1 | employees2
print("The number of employees working in both companies is: ", len(all_employees))

# Sprosit' na uroke
# for i in range(len(all_employees)):
#     input_name = input("Please, enter several names: ")
#     if i == input_name:
#         print("Yes, there are exist such as employee")



# 4. Create 2 collections for storing movies that have been watched by 2 persons,
# get movies that are watched by at least one of them,     : movies - cartoon
# get movies that are watched by 1-st and not watched by 2-nd, print results

# Sprosit' na uroke

# movies1 = {"Moskva slezam ne verit", "Shinel", "Jestoki romams"}
# movies2 = {"Spisok Shinglera", "V jazze tol'ko devushki"}

# person1 = "Stiven"
# person2 = "Melissa"
# person1 = movies1 - movies2

# print(person1, "movies that are watched by 1-st and not watched by 2-nd")
# both_watchers = movies1 & movies2


# 6. Calculate multiplication of elements starting from some inputted number up to other inputted number

num1 = int(input("Please, input the first number: "))
num2 = int(input("Please, input the second number: "))
sum = num1*num2
print("Result of multiplication is: ", sum)


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


# 10. Calculate multiplication of numbers from 0 to inputed value and print it

num3 = 0
num4 = int(input("Please, input the number: "))
calc = num3*num4
print(f"Result of multiplication is: {calc}")



# 11. Input collection of numbers, find last number which square root is less than 26, print it
# napolovinu
# import math
# square_root = input("Please, enter the numbers: ")
# sum = 0
# for i in range(7):
#     sum += i
#     if i < (math.sqrt(25)):
#         break
#     print(sum)

#print (math.sqrt(25))