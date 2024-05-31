thisdict= {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964,
    "year": 2020 
} #key sesitive in case of duplicates it takes value of the most recent declaration
print(thisdict)
print(thisdict["brand"])
print(thisdict["year"])

print(len(thisdict))
print(type(thisdict))

print(thisdict.keys()) #to get all the keys
print(thisdict.values()) #to get all the values
print(thisdict.items()) #return each item in a dictionary as tuples in a list

#as a constructor

mydict= dict(name="John", age= 36, country="Norway")
print(mydict)
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
Dictionary is a collection which is ordered and changeable. No duplicate members.
"""
print("\n")
car= {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
} 

#accessing data from the dictionary
x= car["year"]
print(x)
y= car.get("year")
print(y)

#adding data in dictionary
car["color"]= "black"
print(car)

#replacing/updating(update() can also be used for adding) value
car["year"]=2020
print(car)
car.update({"year": 2021})
print(car)

#removing a value from dictionary
car.pop("model")
print(car)
car.popitem() #removes last added item
print(car)
#then u have classic clear() and del keyword

#copying a dictionary
mydict2= car.copy()
print(mydict2)
mydict3= dict(car)
print(mydict3)


print("\n")
#nested dictionary 1
x_father={
    "name": "John",
    "age": 41
}
x_mother={
    "name": "Emily",
    "age": 36
}
x_child={
    "name": "Tom",
    "age": 12
}
x_family={
    "father": x_father,
    "mother": x_mother,
    "child": x_child
}
#accessing nested dictionary 
print(x_family["father"]["name"])


print("\n")
#nested dictionary 2
family={
    "Father":{
        "Name": "John",
        "Age": 41
    },
    "Mother": {
        "Name": "Emily",
        "Age": 36
    },
    "Child": {
        "Name": "Tom",
        "Age": 12
    }
}
#accessing nested dictionary 
print(family["Father"]["Name"])
print("\n")
for x, obj in family.items():
    print(x)
    for y in obj:
        print(y+":",obj[y])

''' ^^^ VIP understand it ^^^^   '''
