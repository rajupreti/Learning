mytuple= ("apple", "banana", "cherry")
print(mytuple)
print(mytuple[0])
print(len(mytuple))
newtuple= ("apple") #considered as string not tuple
newtuple2= ("apple",) #considered as tuple
print(type(mytuple))
print(type(newtuple))
print(type(newtuple2))

#making tuple constructor
thistuple= tuple(("apple","banana","cherry"))
thistuple2= tuple(("apple"))
print(thistuple)
print(thistuple2)

"""
1. to add/remove values in tuples u have to convert it to string anf back to tuple
2. or you can make a new tuple and add (not remove)
"""

mytuple += newtuple2
print(mytuple)

del thistuple #to delete the tuple

'''Unpacking tuples'''

fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#play with the astrisk (*) to understand
fruits = ("apple","banana","cherry","strawberry","raspberry")
(green,*yellow,red) = fruits
print("\n"+ green)
print(yellow)
print(red)

#Search for the first occurrence of the value 8 using index()
number = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = number.index(8)
print(x)
#count number of occurences of a paticular value in tuple
y= number.count(7)
print(y)