'''
Moataz Khallaf
stacks and queues
Oct 24, 2018
'''
'''
A stack is an order of proccessing information in a list where the most recently added item
is the item that is proccessed first. ('last in first out', LIFO)

analogy : as plates are piled ontop of each other, the plates at the bottom are the first to collected,
but last to be cleaned

'''

# Ex-1 Unfair teacher

print("the unfair teacher always answers")
print("The most recent student first")

stuQuest = [
    "Stewart",
    "Taz",
    "Daj",
    "bobert",
    "Simonuel Jackson"
]

print(stuQuest)
repeat = True
while repeat:
    var = stuQuest.pop()
    print("the unfair teachers answers "+var + "'s question")
    print(stuQuest)

    again = input("")
    if again == "":
        pass
    else:
        repeat = False

'''
Queue is an order of processing information in a list where the first information entered
is the first information processed ("first in first out" FIFO)

Analogy: lining up to get your bus pass.
'''

# Ex-2 the fair teacher

print("the fair teacher answers questions in the order they are asked")

stuQuest2 = [
    "Balony",
    "Jose",
    "igor",
    "Jack",
    "joe"
]

print(stuQuest2)

repeat2 = True
while repeat2:
    print("the fair teacher answers "+ stuQuest2.pop(0) +"'s answer")
    again2 = input("")
    if again2 == "":
        pass
    else:
        repeat2 = False