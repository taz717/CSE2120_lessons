'''
Moataz Khallaf
BlackJack
Oct 24, 2018
'''
import random
from deckOfCards import makeDeck

deck = makeDeck()
num = len(deck)
cardNum = 0

'''
ToDos
1. Make a hand that can store the cards drawn from the deck
2. Make a function to add the total of cards at hand
    HINT: use the first charecter of the data to add a total
3. Make it 2 player
4. Make a PC player
'''
def cardGet():
    var = []
    x = random.randrange(num)
    y = deck[x] ##it's not returning a list
    var.append(y)
    return var

def moreCard():
    x = input("more? Y/n ")
    x = x.lower()
    if x == "y" or x == "yes" or x =="":
        return True
    else:
        return False

def addToList(a, b):
    a.append(b)
    print(a)
    return a

again = True

###real code

while again:
    playerDeck = []
    card = cardGet()
    playerDeck.append(card)
    
    again = moreCard()
print(playerDeck)