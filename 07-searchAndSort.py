'''
Moataz Khallaf
search and sort in lists
Oct 30, 2018
'''

names = ["Peter Parker", "Bruce Wayne", "Clark Kent", "Diana Prince", "Bruce Banner",
 "Tony Stark", "Barry Allen", "Donald Blake", "Malcolm Murdock",
  "Carol Danvers", "Selina Kyle", "Steve Rogers", "Oliver Queen",
   "James Rhodes", "Scott Summers", "J. Jonah Jameson", "Wade Wilson",
    "Hal Jordan", "Scott Pilgram", "Stephen Strange", "Eddie Brock",
     "Lex Luther", "Charles Xavier", "Emma Frost", "Jean Grey", "Victor Von Doom",
      "Frank Castle", "Reed Richards", "Sue Storm", "Johnny Storm", "Ben Grimm", "Erik Lehnsherr",
       "James Howlett", "John Constantine", "Barbara Gordan", "Dick Greyson",
        "Jason Todd", "Time Drake", "Jessica Jones", "Luke Cage", "Danny Rand",
         "Wally West", "Bobby Drake", "Warren Worthington III", "Hank McCoy", "Alex Summers",
          "Kurt Wagner", "Ororo Munroe", "Piotr Rasputin", "Betsy Braddock", "Remy LeBeau",
           "Anna-Marie LeBeau", "Cain Marko", "Raven Darkholme", "Laura Kinney",
            "Pietro Maximoff", "Wanda Maximoff", "Hank Pym", "Janet van Dyne", "Kitty Pryde",
             "Clint Barton", "Natalia Romanova", "Luke Charles", "Samual Wilson",
              "Jennifer Walters", "Barbara Barton", "Maria Hill", "Sharon Carter",
               "Nick Fury", "Mary Jane Watson", "Felicia Hardy", "Gwen Stacy", "Lois Lane",
                "Steve Trevor"]

### Searching
print(names)

sortedNames = []
for i in range(len(names)):
    sortedNames.append(names[i])
'''
#Ex 1 searching for an item in a list

if "Bruce Banner" in names:
            print(True)
if "Bruce" in names: ##Gotta be exact match
    print(True)

#EX 2 partial match in list
for i in range(len(names)):
    if "Bruce" in names[i]:
        print(names[i])

#EX 3 index location of value
var = names.index("Barbara Gordan")
print(var)

#EX index location of partial matches
for i in range(len(names)):
    if "Barbara" in names[i]:
        print(i)
'''
#### Sorting

#EX 5 alpha sorting
sortedNames.sort()
print("")
print("")
print("")

print(sortedNames)

#EX 6 reverse Alpha sort
sortedNames.sort(reverse = True)
print("")
print("")
print("")

print(sortedNames)

##Notes: the order of alpha sorting follows special charectors then numbers then letters

#EX 7 
sortedNames.sort(key = len)
print("")
print("")
print("")

print(sortedNames)

#EX 8
sortedNames.sort(key = len, reverse = True)
print("")
print("")
print("")

print(sortedNames)

'''
The sort.function rearranges the values in the list, therefore their index values
will change
'''