import math
# 1. Define a collection of weekdays, print following: first 5 week days, total days number, last 2 days, odd days

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(weekdays[:5])
print(len(weekdays))
print(weekdays[-2:])


# 2. Define a collection of colors, add a color from console, print total colors number, print colors on even positions

colors = ["Red", "Green", "Blue", "Gray", "Yellow", "White"]
color = input('Please, enter color name: ')
colors.append(color)
print(colors)
print(len(colors))
print(colors[1::2])


# 4. Define collection of students (names) from group 1 and collection of students from group 2, print the collection of students from both groups

group1 = ["Ann", "Bob", "Sam"]
group2 = ["Jhon", "Tom", "Kevin"]
print(group1 + group2)


# 6. Define a collection of programming languages (names), add new language name from console if it’s not C#
#????????????
languages = ["Python", "Java"]
language = input("Please, enter the language:")
languages.append(language)
print(languages)


# 7. Define an empty collection, input 3 numbers and add them to collection, calculate factorial for the last one

numbers = []
n = int(input('Enter the number: '))
numbers.append(n)
print(math.factorial(n))


# 8. Define a collection of words, input 2 new words and add them to list, find some inputed word in list and remove a word with some inputed index

words = ["Large", "Big", "Small", "Tall"]
word = input("Please, enter a word:")
words.append(word)
print(words)
print(words[3])
words.pop(2)
print(words)