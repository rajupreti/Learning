def basic():
    print("Hello World")

basic()

#functions with arguments/parameters
print("\n")
def name(fname):
    print("The name of the person is", fname)
name("Raj")
name("Sophie")

'''
By default, a function must be called with the correct number of arguments. 
Meaning that if your function expects 2 arguments, 
You have to call the function with 2 arguments, 
Not more, and not less
'''
print("\n")
def names(fname,lname):
    print(fname+"&"+lname)
names("Raj","Sophie")

#Arbitrary Arguments, *args
print("\n")
def arbarg(*family):
    print("Youngest in the family is", family[2])
arbarg("father","mother","child")

#Keywords Arguments
print("\n")
def keyarg(child1,child2,child3):
    print("Youngest in the family is", child3)
keyarg(child3 = "John", child2 = "Tom", child1 = "Jennifer")

#Arbitary Keyword Arguments, **args
#If you do not know how many keyword arguments that will be passed into your function
print("\n")
def keyarbarg(**friends):
    print(friends["friend2"],"is my best friend.")
keyarbarg(friend1="Joey",friend2="Chandler",friend3="Ross")

#Default Parameter Value
print("\n")
def dpv(country="India"):
    print("I am from", country)
dpv("France")
dpv()
dpv("United Kingdom")

print("\n")
#Passing a List as an argument
def las(food):
    for x in food:
        print("I like", x)
fruits= ["apple", "banana", "cherry"]
las(fruits)

print("\n")
#Position only (x, /) & Keyword only (*, x) arguments
def pko (w, x, /, *, y, z):
    print("Sum is", w+x+y+z) 
pko(1, 2, y=3, z= 4)

print("\n")

print("\n")
#Recursion using functions
def ruf(k):
    if k > 0:
        result = k + ruf(k-1)
        print(result)
    else:
        result = 0
    return result
print("Recursion result example: ")
ruf(6)