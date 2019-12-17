import re

# 1. Input one string, define another one, concatenate them and print the result

# with input()
print("Please, enter the word and press enter to see concatenation.")
string1 = input()
string2 = " - is test for Python concatenation."
print(string1 + string2)

str1 = "This is my "
str2 = "homework"
print(str1 + str2)

# 2. Define multiline string and print it

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

# 3. Input a string and get substring from start to some position

sub_str = input("Please, enter the word.")
print(sub_str[0:4])

# 4. Define a string and get substring of even elements

even = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(even[1::2])

# 5. Input a string, print it from start to half if its length is even, otherwise from half to the end

text = input("Please, enter a word: ")
if (len(text)) % 2 == 0:
    print(text[:len(text)//2])
else:
    print(text[len(text)//2:])


# 6. Calculate number of  ‘d’ chars in inputed string

word = input('Please, enter word with several symbol \'d\'.')
character = "d"
number = word.count(character)
print("The number of character \"d\" is:", number)


# 7. Input string of words separated by coma, get number of words and print it

word = "first, second, third, fourth, fifth, sixth, seventh"
result = len(word.split())
print ("The number of words is : " + str(result))

# with input()
word = input("Please, enter string of words separated by coma: ")
result = len(word.split())
print ("The number of words is : " + str(result))


# 8. Input string, find how many ‘ab’-s are inside

word = input("Please, enter string with \"ab\" symbols:")
symbol = word.count("ab")
print(symbol, " \"ab\" - in this string.")


# 9. Input string and replace all ‘1’ with ‘one’

text = input("Please, enter string with \"1\" symbol: ")
change_text = text.replace("1", "one")
print(change_text)


# 10. Define a string with values inside using format() method and print result

format1 = "We are learning {language} version {version}.".format(language = "Python", version = 3)
print(format1)

format2 = "We are learning {0} version {1}.".format("Python", 3)
print(format2)

format3 = "We are learning {} version {}.".format("Python", 3)
print(format3)


# 11. Create a regular expressions to check if string meets some requirements

str = "I am doing homework"
reg = re.search("^I am doing homework$", str)

if (reg):
  print("We have a match!")
else:
  print("No match")


# 12. Create a regular expression to find occurence of regular expression in strings

str = "food good foot moon"
reg = re.findall("oo*", str)
print(reg)
if (reg):
  print("We have a match!")
else:
  print("No match")