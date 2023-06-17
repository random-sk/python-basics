''' Welcome to my experimentation 
with Python Basics! ~Sei-Bon Kim '''

# TODO: Make code and printed 
# statements easier to read, get rid of similar code

# Basic statements and syntax rules
print("") # Prints an empty line
print("This was outputted using the print statement, followed by a new line")
if 2 > 1:
	print('When using if, add : after the condition and consistently indent the statements')
print("") 

# Variable assignment and casting
string = "This is a variable and so is the next line!"
number = 3
print(string)
print(number)
number = "Variables aren't declared types and can change types, however can be cast as e.g. str, int or float"
print(number)
x = str(4)
y = int(4)
z = float(4)
print(x, y, z)
print("Variables must start with a letter/underscore, can contain numbers, and are case-sensitive:")
myVariableName = "camelCase"  
MyVariableName = "PascalCase" 
my_variable_name = "snake_case"
print(myVariableName, MyVariableName, my_variable_name)
X, Y, Z = "Many variables can be assigned", "in one line and can be printed", """using only one print statement:
Comma automatically create a space, plus doesn't but adds together numbers & concatenate strings/other variables of the same type"""
print(X, Y + " " + Z)
print(y + z)
a = b = c = "These 3 variables are equal"
print(a, b, c)
sentence = ["Collections", "can be", "unpacked"] # Including tuples
A, B, C = sentence
print(A, B, C)
print("")

# Functions and global/local variables
variable = "This is a global variable that can be accessed by any function"
def gvFunc():
	print(variable)
gvFunc()
def lvFunc():
	variable = "This is a local variable that can only be accessed by this function"
	global gloVar
	gloVar = "This is a global variable declared inside a function"
	print(variable)
lvFunc()
print(gloVar)
gloVar2 = "Another global - this won't be outputted"
def localFunc():
	global gloVar2
	gloVar2 = "Functions can declare an already existing global variable as global"
	print(gloVar2)
localFunc()
print("")

# Creating variables of different data types, and outputting the types
def pd():
	print(d, type(d))
d = "Hi"
pd()
d = 10
pd()
d = 10.2
pd()
d = 2j
pd()
d = ['Dog', 'Cat', 'Mouse'] 
pd()
d = ('dog', 'cat', 'mouse')
pd()
d = range(4)
pd()
d = {'height' : '150cm', 'weight' : '50kg'}
pd()
d = {'ice', 'water', 'steam'}
pd()
d = frozenset({'Ice', "Water", 'Steam'})
pd()
d = True
pd()
d = b"Hi"
pd()
d = bytearray(6)
pd()
d = memoryview(bytes(6))
pd()
d = None
pd()
print("")

# Some more casting
d = list(('Tuple', 'cast to', 'list'))
pd()
d = dict(word1="Cast", word2="dict")
pd()
d = set(('tuple to set', '*', '.'))
pd()
d = bool(3)
pd()
d = bytes(4)
pd()
d = int(1.6)
pd()
print("")

# Some more number-related data examples
d = 20e2
pd()
d = 5+3j
pd()
print("")

# Random generator
print("The following is a random integer between 1 and 4 inclusive")
import random
print(random.randrange(1, 5)) 
print("")

# Manipulating strings
d = "Strings are arrays and you can get characters from them, such as:"
pd()
print(d[1])
print("For Loop prints every character in the word: apple")
for c in "apple":
	print(c)
d = "The length of this sentence is:"
pd()
print(len(d))
d = "There is the word ~is~ in this sentence"
pd()
d = "is" in d
pd()
if "is" in "There is a word": # Membership operator
	print("yes, is")
d = "This is a sentence that doesn't contain the opposite of true"
pd()
d = "false" not in d
pd()
d = "The first word of this will be sliced twice (second index not included)"
pd()
print(d[0:3], d[:3])
d = "Now the last word"
pd()
print(d[13:])
d = "The first index is not included for negative indexes"
pd()
print(d[-7:-2])
d = " Let's use upper, lower, strip, replace, and split "
pd()
print(d.upper())
print(d.lower())
print(d.strip())
print(d.replace("s", "$"))
print(d.split(" "))
text = "The quantity {} has been formatted, as well as the price of {} dollars"
age, price = 10, 20
print(text.format(age, price))
text2 = "This has been ordered correctly: {2} minus {1} is {0}"
numBig, numMed, numSmall = 30, 20, 10
print(text2.format(numSmall, numMed, numBig), "\n")

# Escape characters
print("Strings can contain \"quotes\" like this through the use of \\, \nand can start on a new line")
print("\tThat was a tab, this is backspace\b, this is carriage return\r")
print("\tThis is tab, carriage return\r, then octal value\ooo")
print("Hex value \"\\xhh\" also an escape char\n")

# More string methods
d = "the first letter is capitalized"
print(d.capitalize())
d = "CASEFOLD is the same as LOWER, this sentence will be encoded and contains one instance of the letter z"
print(d.casefold().center(10))
print(d.count("z"))
print(d.encode())
print("Does the 2nd string of this section end with letter z?", d.endswith("z"))
d = "you can set \tthe tab size of the string"
print(d.expandtabs(50))
print("The letter c in the previous string is located in position:", d.find("c"))
d = "Format_map"
print(d.format_map(1))
d = "Index is the same as Find, the first letter x is located:"
print(d, d.index("x"))
d = "This sentence contains symbol @ so is it alphanumeric?"
print(d, d.isalnum())
d = "This sentence contains number 1 which isn't in the alphabet."
print(d, d.isalpha())
d = "10000"
print(d, d.isdecimal(), d.isdigit(), d.isidentifier(), d.isnumeric(), d.isprintable(), d.isspace(), d.istitle())
d = "Is this sentence all upper or all lower?"
print(d, d.isupper(), "and", d.islower())
d = "This is a joined letter:"
print(d, d.join("A"))
d = "      Left/Right justified/stripped?         "
print(d.ljust(1))
print(d.rjust(1))
print(d.lstrip())
print(d.rstrip())
d = "Testing testing"
print(d.maketrans("Test", "West"))
d = "Let's split this into three"
print(d.partition(" "))
print(d.rpartition(" "))
d = "Test"
print(d, d.replace("T", "W"))
d = "Where is the last instance of the letter o?"
print(d, d.rfind("o"), "Again,", d.rindex("o"))
d = "R split and strip               "
print(d.rsplit())
print(d.rstrip(" "))
d = "Let's...\nreturn a list"
print(d.splitlines())
d = "Does this sentence start with D?"
print (d, d.startswith("D"))
print("swapcase version:", d.swapcase(), "title version:", d.title(), "translation:", d.translate("Testing"))
d = "This line has three 0 values at the beginning"
print(d.zfill(3), "\n")

# Working with booleans
no1 = 100
no2 = 50
if no2 > no1:
	print("No2 is bigger")
else:
	print("No1 is bigger")
print(bool("Hi"), bool(""), bool([]))
class Class():
	def __len__(self):
		return 0
obj = Class()
print(bool(obj))
def returnsTrue():
	return True
print(returnsTrue())
print(isinstance(no1, str), "\n")

# Arithmetic operators
a = 4
b = 3
print(a+b, a-b, a*b, a/b, a%b, a**b, a//b, "\n")

# Assignment operators
d = 10
pd()
d += 4
pd()
d -= 3
pd()
d *= 2
pd()
d /= 2
pd()
d %= 6
pd()
d //= 2
pd()
d **= 3
pd()
d = int(d)
d &= 8
pd()
d |= 3
pd()
d ^= 2
pd()
d >>= 3
pd()
d <<= 2
pd()

# Comparison Operators
a = 7
b = 3
if a == b:
	print("a is equal to b")
if a != b:
	print("\na isn't equal to b")
if a >= b:
	print("a is greater than/equal to b\n")

# Logical Operators
if (a > 5 and b > 5) or not(b == 5):
	print("Example of logical operators returning true")

# Identity operators
if a is b:
	print("a is b")
if a is not b:
	print("a isn't b")

# Bitwise Operators for binary numbers
b0, b1 = 0, 1
print(b0, "&", b1, b0&b1, b0|b1, b0^b1, ~b0, b1<<2, b1>>2)

'''Highest precedence to lowest: (then left to right)
(), **, {+x, -x, ~x}, {*, /, //, %}, (+, -), (<< >>), &, ^, |,
{comparison, identity, membership operators}, not, and, or'''

# Lists - can contain different data types, ordered & changeable. (Tuple = unchangeable list.
# Set is unordered, unchangeable, unindexed, no duplicates. Dictionary is ordered, changeable, no duplicates.)
snakes = ["python", "cobra", "adder", "python"]
print("\nThere are", len(snakes), "items in my list of snakes. The second item is", snakes[1])
print("The third item is", snakes[-2])
print(snakes[1:3])
print(snakes[-4:])
if "cobra" in snakes:
	print("cobra snake")
snakes[3] = "rattlesnake"
snakes[1:3] = "adder", "cobra"
snakes[:1] = "python", "python"
print(snakes)
snakes[1:3] = ["adder"]
[print(x) for x in snakes]
snakes.insert(1, "viper")
snakes.append("basilisk")
j = 0
while j < len(snakes): # can be done with tuple
	print(snakes[j])
	j += 1
reptiles = ["gecko", "skink"]
reptiles.extend(snakes)
reptiles.remove("basilisk")
reptiles.pop(2)
reptiles.pop()
for x in reptiles: # can be done with tuple + set
	print(x)
del reptiles[2]
for i in range(len(reptiles)): # tuples too
	print(reptiles[i])
print(reptiles.clear(), "\n")
del reptiles

# List comprehension for shorter syntax
veg = ["carrot", "potato", "onion"]
vegT = []
for x in veg:
	if "t" in x:
		vegT.append(x)
print(vegT)
vegT2 = [x for x in veg if "t" in x] #[EXPRESSION for ITEM in ITERABLE if CONDITION == TRUE]
print(vegT2)
print([x for x in veg if x != "potato"])
print([x for x in veg])
print([x for x in range(2)])
print([x for x in range(20) if x < 7])
print([x.title() for x in veg])
print(["lettuce" for x in veg])
print([x if x != "onion" else "garlic" for x in veg], "\n")

# Sorting lists
veg.sort()
print(veg)
numList = [2, 5, 1, 3, 4]
numList.reverse()
print(numList)
numList.sort()
print(numList)
numList.sort(reverse = True)
print(numList)
def closeTo3(n):
	return abs(n-3)
numList.sort(key = closeTo3)
print(numList)
colour = ["red", "Green", "blue"]
colour.sort() #case-sensitive
print(colour)
colour.sort(key = str.lower) #case-insensitive
print(colour)

# Copying/joining lists
list1 = ["Changes to this will change", "list1", "and list2"]
list2 = list1
print(list1, list2)
list1.append("!")
print(list1, list2)
list3 = ["So", "use", "copy/list"]
list4 = list3.copy()
list5 = list(list3)
list3.append("!")
print(list3, list4, list5)
list4 = list4 + list5
for x in list4:
	list3.append(x)
print(list3)

# Extra list methods - can also be done for tuples
binaryList = [0, 1, 1, 0, 1, 1]
print("\nThe number of zeros is:", binaryList.count(0), "\nThe position of the first 1 is:", binaryList.index(1))

# Tuple basics - elements can be of any data type and can be accessed through indexes
d = ("\nThis is just a string")
pd()
d = ("This is a 1-length tuple",)
pd()
print(len(d))
d = ["List can", "be cast", "to tuple"]
pd()
print(tuple(d))
if "be cast" in d:
	print("the above tuple contains the word cast")

# Updating tuples
shadeT = ("Black", "white")
shadeL = list(shadeT)
shadeL[1] = "White"
shadeL.append("Grey")
shadeT = tuple(shadeL)
paints = ("Red", "Blue", "Green")
paints += shadeT
print(paints)
del shadeT

# Unpacking and multiplying tuples
rattlesnake = ("scales", "rattle", "eyes", "fangs")
(body, tail, *face) = rattlesnake
print(body, tail, face)
cities = ("Auckland", "Wellington", "Christchurch", "Sydney")
(*north, south, neither) = cities
print(north, south, neither)
print(cities*2, "\n")

# Sets - do not allow duplicate values like True and 1
mySet = {True, False, 1, 2,}
print(mySet, "is of length", len(mySet))
print("Does the set contain item 5?", 5 in mySet)
mySet.add(3)
mySet2 = {4, 5}
myList = [6, 7]
myTuple = (8, 9)
myDict = {10 : 11, 12 : 13}
mySet.update(mySet2)
mySet.update(myList)
mySet.update(myTuple)
mySet.update(myDict)
print(mySet)
mySet.remove(False)
mySet.discard(True)
mySet.pop()
print(mySet)
mySet.clear()
print(mySet, "\n")
del mySet

# More on joining sets
uppers = {"A", "B", "C"}
lowers = {"a", "b", "c"}
letters = uppers.union(lowers)
print(letters)
snakeSet = {"Python", "Cobra", "Adder"}
programLang = {"Python", "C", "Java"}
snakesAndLang = snakeSet.intersection(programLang)
snakeSet.intersection_update(programLang)
print(snakesAndLang, snakeSet)