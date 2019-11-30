# 1. Define a collection of numbers, generate a new collection selecting only odd or dividable by 6 numbers and print it

nums = [15, 22, 31, 36, 44, 60, 73]
check_nums = [i for i in nums if i % 2 == 1 or i % 6 == 0]
print(check_nums)

# 2. Create a collection of 6 names inputed from console , generate a new collection selecting only the names starting from ‘A’ and print it

names = []
print("Please, enter 6 names, also started with letter A: ")
for i in range(6):
    name = input()
    names.append(name)
check_names = [name for name in names if name.startswith("A")]
print(check_names)

# 3. Define a collection of color names, generate a new collection selecting only color name having more than 1 ‘o’ and print it

colors = ["white", "black", "yellow", "maroon", "chocolate", "brown"]
check_colors = [i for i in colors if i.count ("o") > 1]
print(check_colors)


# 4. Define a collection of pets, that stores types of pet and its name, find how many pets have name Johny and print the number

pets = {
    "Dog"    : "Johny",
    "Cat"    : "Murka",
    "Parrot" : "Kesha",
    "Rabbit" : "Johny"
}
sum = 0
for i in list(pets.values()):
    if i == "Johny":
        sum += 1
print(sum)

# 5. Create a collection for storing hotel visitors (name, country), input several visitors from console,
# print how many visitors are now in hotel, what is their country, what is their name

visitors = {
    "Stanislav" : "Russia",
    "Georgy" : "Georgia",
    "Kevin"  : "USA",
    "Duane"  : "Australia"
}
for i in range(2):
    name = input("Please, enter the visitor name: ")
    country = input("Please, enter the visitor country: ")
    visitors[name] = country
print(visitors)

# Case 1 - print how many visitors are now in hotel
sum = 0
for i in list(visitors.keys()):
    sum += 1
print(sum)

#or
print(len(visitors))

# Case 2 - what is their country
print("Their countries are: ")
for name in visitors.values():
  print(name)

# Case 3 - what is their name
print("Their names are: ")
for country in visitors.keys():
  print(country)

# or
print("Their names and countries are: ")
for name, country in visitors.items():
  print(name, " : " + country)


# 6. Create a collection of students with their scores and input them from console, remove students with score less than 40 and print final collection

students = {}
for i in range(2):
    name = input("Please, enter the student's name: ")
    score = int(input("Please, enter the student's score: "))
    students[name] = score
for i in list(students):
    if students[i] < 40:
        students.pop(i)
print(students)

# 7. Create a collection of dates (date like ‘1/11/2018’ with weekday like ‘Monday’), print total number of date, dates for non-working days (Saturday, Sunday)

dates = {
      "Sunday"
      : '1/11/2018',
      "Monday"    : '2/11/2018',
      "Tuesday"   : '3/11/2018',
      "Wednesday" : '4/11/2018',
      "Thursday"  : '5/11/2018',
      "Friday"    : '6/11/2018',
      "Saturday"  : '7/11/2018'
}

# Case 1 - print total number of date
sum = 0
for i in list(dates.keys()):
    sum += 1
print(sum)

# Case 2 - print dates for non-working days (Saturday, Sunday)
non_working1 = dates.get("Saturday")
non_working2 = dates.get("Sunday")
print(non_working1)
print(non_working2)


# 8. Create a collection of filenames with their size, print how many files are greater than 15Mb, how many filenames start from ‘a’ letter, increase size of the file which name ends with ‘.txt’

filenames = {
     "any.psd"       : "30MB",
     "second.py"     : "25MB",
     "third.cpp"     : "20MB",
     "anything.html" : "15MB",
     "fifth.txt"     : "10MB"
}

# Case 1 - print how many files are greater than 15Mb

sum = 0
for i in list(filenames.values()):
    if i > "15MB":
        sum += 1
print(sum)

# Case 2 - how many filenames start from ‘a’ letter

sum = 0
for i in list(filenames.keys()):
    if i.startswith(('a')):
        sum += 1
print(sum)

# Case 3 - increase size of the file which name ends with ‘.txt’

filenames["fifth.txt"] = "25MB"
print(filenames)