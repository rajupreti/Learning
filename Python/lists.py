thisList =  ["apple", "banana", 23, False,"mango"]
print(thisList[-1])
print(thisList[-4:-1])
print(thisList)

#replace a value in list
thisList[3]= "strawberry"
thisList[2]= "blueberry"
print (thisList)

#insert a value inbetween list
thisList.insert(2,"watermelon")
print(thisList)

#add new value to list
thisList.append("grapes")  #add at the end of list
print(thisList)
thisList.insert(0,"cherry") #add at the beginning of the list
print(thisList)

#add 2 different lists (u can use the same function with a tuple)
tropical= ["papaya","pineapple"]
thisList.extend(tropical)
print(thisList)

#removing list items
thisList.remove("banana")
print(thisList)

thisList.pop(1) #removes the mentioned value
print(thisList)
del thisList[0]
print(thisList)

thisList.pop() #removes the last value if nothing is mentioned
print(thisList) 

thisList.clear() #list will be there but it will contain no values
print(thisList)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): #for loop in list
  print(thislist[i])

#list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#same as the previous
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#other ways of list comprehension
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sorting in lists

numbers = [100, 50, 65, 82, 23]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)  #for desending sort
print(numbers)

#customised sorting
def myfunc(n):
  return abs(n-50)

numbers.sort(key= myfunc)
print(numbers)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#deletes the whole list 
del numbers  
print(numbers)
