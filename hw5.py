import re

#*Input one string, define another one, concatenate them and print the result

print("Please, enter the word and press enter to see concatenation")
string1 = input()
string2 = " - test for Python concatenation"
print(string1 + string2)

str1 = "This is my "
str2 = "homework"
print(str1 + str2)

#*Define multiline string and print it

multiline1 = '''
 First line
 Second line
 Third line
'''
print(multiline1)


multiline2 = """
 Fourth line
 Fifth line
 Sixth line
"""
print(multiline2)


#*Input a string and get substring from start to some position

substring = "homework"
print(substring[0:4])


#*Define a string and get substring of even elements

even = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(even[1::2])


#*Calculate number of  ‘d’ chars in inputed string

words = "drop down drop down"
character = "d"
number = words.count(character)
print("The number of character d is:", number)


#*Input string of words separated by coma, get number of words and print it

word = "first, second, third, fourth, fifth, sixth, seventh"
result = len(word.split())
print ("The number of words are : " + str(result))


#*Input string, find how many ‘ab’-s are inside

str = "ab ab ab ab ab".count('ab')
print(str)


#Input string and replace all ‘1’ with ‘one’

text = "This is the 1 and other 1"
txt = text.replace("1", "one")
print(txt)


#*Define a string with values inside using format() method and print result

format1 = "We are learning {language} version {version}.".format(language = "Python", version = 3)
print(format1)

format2 = "We are learning {0} version {1}.".format("Python", 3)
print(format2)

format3 = "We are learning {} version {}.".format("Python", 3)
print(format3)


#Create a regular expressions to check if string meets some requirements

str = "I am doing homework"
reg = re.search("^I am doing homework$", str)

if (reg):
  print("We have a match!")
else:
  print("No match")


#*Create a regular expression to find occurence of regular expression in strings

str = "food good foot moon"
reg = re.findall("oo*", str)
print(reg)
if (reg):
  print("We have a match!")
else:
  print("No match")