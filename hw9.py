# 1. Input 3 collections of numbers, calculate how many numbers are greater than 10 for first,
# how many numbers are greater than 20 for second and how many numbers are greater than 30 for third collection
# (implement version without functions and version with functions)

# Version without function

# collection = []
# count = 0
# for i in range(3):
#     print("Please, input number to the first collection: ")
#     first_collection = int(input())
#     # collection.append(first_collection)
#     if i > 10:
#         count +=1
# print(count)



# first_collection = []
# print("Please, input 3 numbers: ")
# count = 0
# for i in range(3):
#     num = int(input())
#     first_collection.append(num)
#
# check_collection = [num for num in first_collection if num >10]
# count += 1
# print(count)




# Version with functions

numbers = ()

print("Please, input 3 numbers: ")
def number_coounter(number):
    count = 0
    for i in number():
        num = int(input())
        if num > 10:
            count +=1
            print(count)
# number_coounter(number)



# 2. Input a collection of numbers, calculate how many numbers are positive and dividable by 6 (create a function),
# generate a new collection of odd numbers (create a function), print results


# digits = ()
# #input
# def positiv_devide(digs):
#     sum = 0
#     # input#input
#     for i in digs:
#         if i < 0 and i %6 == 0:
#             sum += 1
#     return sum
# print(positiv_devide(i))


