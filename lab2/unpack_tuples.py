#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
#Assign the rest of the values as a list called "red":
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green1, yellow1, *red1) = fruits1

print(green1)
print(yellow1)
print(red1)

#Add a list of values the "tropic" variable:
fruits2 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green2, *tropic, red2) = fruits2

print(green2)
print(tropic)
print(red2)