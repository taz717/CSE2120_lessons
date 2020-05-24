'''
Moataz Khallaf
Make a sandwich
Oct 23, 2018
'''

### inputs
def askItem():
    x = input("What item you wanna add g?")
    return x

###processing
def addToList(item, list):
    list.append(item)
    return list

def again():
    x = input("more? Y/n")
    x = x.lower()
    if x == "y" or x == "yes" or x =="":
        return True
    else:
        return False

###output
def prList(x):
    print("your sanny has", x)

### Code start ###
##vars
swich = []
repeat = True
while repeat:
    ingredient = askItem()

    swich = addToList(ingredient, swich)

    prList(swich)

    repeat = again()