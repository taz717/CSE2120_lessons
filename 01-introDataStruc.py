'''
Moataz Khallaf
intro to data structures
Oct 22 , 2018
'''

##Notes yaaay
'''
a data structure is an organizational manegement and formating tool for data.
It provides effecient access and modification to data.

Primitive data types include strings, integers and floats. Data structures include
lists and arrays. Some of these are modifyable and some are not

Advanced data structure include data bases and neural netwoeks.
'''

''' Tuples
non editable list of primitive data
'''
##EX-1 charectors in strings
var = "Hello World"
print(var[2]) #The number indicated which charector to display
print(var[2:7]) #range between charector 2 to 5
print(var[5:]) #range between 5 to end

##EX-2 Tuple
var2 = ('hello', 'world', 'three', 'APPLE!!') #off by one logical error
print(var2) #prints all items in tuple
print(var2[2]) #prints third item
print(var2[2][3]) #prints the 4th charector of the third word

##EX-3 Add some random
import random

x = len(var2) #counts how many items are in a tuple
print(x)

getNum = random.randrange(x) #get a random integer from the total items in var 2 tuple
print(getNum) #print said number
print(var2[getNum]) #print value in Tuple

#aside
var3 = (
    "apple",
    "banana",
    "orange",
    "mango"
)

