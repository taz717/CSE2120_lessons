'''
Moataz Khallaf
Make a deck
Oct 23, 2018
'''

suits = (" diamonds", " clubs", ' hearts', ' spades')
face = ["jack", "king", "Queen"]

numbers = []
for h in range(len(suits)):
    for i in range(1, 11): #1 to 10
        numbers.append(str(i)+suits[h])
for h in range(len(suits)):
        for i in range(1, 3):
            numbers.append((face[i]) + suits[h])

print(numbers)