'''
Moataz Khallaf
One dimensional array
Oct 23, 2018
'''
''' Arrays
One Dimensional array are similar to tuples except values can be modifed, added to and taken away.
Dimensional array are often called lists because they list modifiable data
(Two dimensional arrays are called tables)

lists use [] instead of ()
'''

#EX 1 create a list
sandwich = [
    "bread",
    "meat",
    "egg",
    "mustard",
    "mayo"
]

#print(sandwich)

#Ex 2 modify an item
sandwich[3] = "cheese"
print(sandwich)

#Ex 3 adding item
sandwich.append("lettuce")
print(sandwich)
sandwich.insert(2, "bacon")

#Ex 4 removing item
#sandwich.remove("cheese")
sandwich.pop(3)
print(sandwich)