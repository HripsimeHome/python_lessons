# 3. Define some collection of names and get the collection of their first 3 characters using map(), print the result

names = ['Melissa', 'Stiven','Mike', 'Robert']
characters_list = print(list(map(lambda x : x[0:3], names)))

# 4. Input 2 collections of numbers, get the collection where each i-th element is square sum of corresponding elements
# in that 2 collections, print result

first_collection = []
print("Please, enter 2 numbers: ")
for i in range(2):
    num = int(input())
    first_collection.append(num)

second_collection = []
print("Please, 2 numbers: ")
for i in range(2):
    num = int(input())
    second_collection.append(num)

result_collection = print(list(map(lambda x, y: x*y, first_collection, second_collection)))

# 5. Create a collection of flowers with their color, get the flowers which color is red, print result

flowers =[
    {'flower': 'Rose', 'color': 'white'},
    {'flower': 'Poppy', 'color' : 'Red'},
    {'flower': 'Gladiolus', 'color': 'Purple'},
    {'flower': 'Tulip', 'color': 'Red'},
]
print(list(filter(lambda x : x['color']=='Red', flowers)))

# 6. Calculate subtraction of numbers collection using reduce.

import functools
numbers = [500, 200, 50]
print(functools.reduce(lambda x, y : x-y, numbers))


# 7. Create several packages (some nested), several modules inside, call them from outside and use

# Created packages (in package folder). For package homework nested packages are calculations, loops;
# for product package nested packages are lambda_example, reduce_example
# call them from use_package.py from root