'''
Moataz Khallaf
keyword cypher
Oct 30, 2018
'''

code={
    "a":"d",
    "b":"e",
    "c":"a",
    "d":"t",
    "e":"h",
    "f":"b",
    "g":"c",
    "h":"f",
    "i":"g",
    "j":"i",
    "k":"j",
    "l":"k",
    "m":"l",
    "n":"m",
    "o":"n",
    "p":"o",
    "q":"p",
    "r":"q",
    "s":"r",
    "t":"s",
    "u":"u",
    "v":"v",
    "w":"w",
    "x":"x",
    "y":"y",
    "z":"z"
}

print("clue: the debt that everyone pays")

message = input("what is the msg ")
message = message.lower()

var = []
for i in range(len(message)):
    var.append(message[i])


for i in range(len(var)):
    if var[i] in code:
        var[i] = code[var[i]]

encrypt = "".join(var)
#.join joins all values in list using the charectors in qutations to seperate them
print(encrypt)

code={
    "d":"a",
    "e":"b",
    "a":"c",
    "t":"d",
    "h":"e",
    "b":"f",
    "c":"g",
    "f":"h",
    "g":"i",
    "i":"j",
    "j":"k",
    "k":"l",
    "l":"m",
    "m":"n",
    "n":"o",
    "o":"p",
    "p":"q",
    "q":"r",
    "r":"s",
    "s":"t",
    "u":"u",
    "v":"v",
    "w":"w",
    "x":"x",
    "y":"y",
    "z":"z"
}

message1 = input("what is the msg ")
message1 = message.lower()

var1 = []
for i in range(len(message1)):
    var1.append(message1[i])


for i in range(len(var1)):
    if var1[i] in code:
        var1[i] = code[var1[i]]

encrypt1 = "".join(var1)
#.join joins all values in list using the charectors in qutations to seperate them
print(encrypt1)