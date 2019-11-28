import functools
numbers = [500, 200, 50]
print(functools.reduce(lambda x, y : x-y, numbers))