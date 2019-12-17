import math
# 1. Define a collection of weekdays, print following: first 5 week days, total days number, last 2 days, odd days

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(weekdays[:5])
print(len(weekdays))
print(weekdays[-2:])
print(weekdays[::2])

# 2. Define a collection of colors, add a color from console, print total colors number, print colors on even positions

colors = ["Red", "Green", "Blue", "Gray", "Yellow", "White"]
color = input('Please, enter color name: ')
colors.append(color)
print(colors)
print(len(colors))
print(colors[::2])

# 4. Define collection of students (names) from group 1 and collection of students from group 2, print the collection of students from both groups

group1 = ["Ann", "Bob", "Sam"]
group2 = ["Jhon", "Tom", "Kevin"]
print(group1 + group2)

# 5. Define a garage collection that stores 3 cars (models), it’s known that double of same models came to garage, print garage models

garage_list = ["Nissan", "Toyota", "Opel"]
garage_list = garage_list*2
print(garage_list)

# 6. Define a collection of programming languages (names), add new language name from console if it’s not C#

languages = ["Python", "Java", "PHP"]
print("Please, enter 3 languages: ")
for i in range(3):
    lang = input()
    if not(lang.startswith('C#')):
        languages.append(lang)
print(languages)

# 7. Define an empty collection, input 3 numbers and add them to collection, calculate factorial for the last one

numbers = []
print("Please, enter 3 numbers: ")
for i in range(3):
    n = int(input())
    numbers.append(n)
print(math.factorial(numbers[-1]))

# 8. Define a collection of words, input 2 new words and add them to list, find some inputted word in list and remove a word with some inputed index

words = ["Large", "Big", "Small", "Tall"]
word1 = input("Please, enter a first word:")
word2 = input("Please, enter a second word:")
words.append(word1)
words.append(word2)
print(words)
print(words[:-1])