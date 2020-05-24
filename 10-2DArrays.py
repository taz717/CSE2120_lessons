'''
Moataz Khallaf
2D arrays
Oct 31, 2001
'''

''' 2D Arrays 
Two dimensional arrays are lists that have lists within each index value.
2D arrays are often described as tables because the main list will order the subsequent lists within as
as rows or columns

EX row = [[col1, col2], [col1, col2]]
'''

### creating 2d arrays
##EX 1 simple 2d array

ex1 = [[0,0],[100,100],[150,200]]

##EX 2 using a for loop
ex2 =[]
for i in range(1, 6):
    ex2.append([i, i**2])
'''
ex2.append(1,1**2)
ex2.append(2,2**2)
ex2.append(3,3**2)
ex2.append(4,4**2)
...
'''
print(ex2)

##EX3 nested for loop
ex3 = []
for i in range(10):
    ex3.append([])
    for j in range(10):
        ex3[i].append(i+j)
#print(ex3)

###calling and updating values
##using Example 2

#ex5 call a list within a list
print(ex2[1])

#ex6 call an item in a sublist
print(ex2[1][1])

#ex7 updating a value in a sublist
ex2[2][0] = 0
print(ex2)

#Ex7 updating a value in all sublists
for i in range(len(ex2)):
    ex2[i][0] += 5
print(ex2)

