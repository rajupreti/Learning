"""Variables"""
fruits= ['apple', 'banana', 'orange']
vegetables= ['spinach','carrot','beans']
x,y,z= fruits
a=b=c= vegetables
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)

"""Output Variables"""
name='Raj'
age=22
school='SKEMA'
print(name+school) #You cannot do (str+int); it should always be (str, int)
print(name,school)
print(name+school,age)


"""Global Variables"""
s=r=q= "awesome"

def myFunc():
    global s
    r= "fantastic"
    s= "supreme"
    print("Python is", q)
    print("Python is", r)

myFunc()

print("Python is", s)

exit()