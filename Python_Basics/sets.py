#sets are multiple items in a single variable

thisset= {"apple", "banana", "cherry"}
print(thisset)

#the values True and 1 are considered the same value in sets, and are treated as duplicates
#same goes for False and 0
myset= {"apple","banana","cherry",True,1,4}
print(len(myset))
print(type(myset))

#set as constructor
newset= set(("apple","banana","cherry"))
print(newset)
print(type(newset))

#adding in set
print("banana" not in thisset)
thisset.add("orange") #add when adding a value(s)
print(thisset)

tropical= {"pineapple","mango","papaya"}
thisset.update(tropical) #update when adding two sets
print(thisset)
#The object in the update() method does not have to be a set
#it can be any iterable object... tuples, lists, dictionaries etc
berry= ("strawberry","wildberry")
thisset.update(berry)
print(thisset)

#you can remove item in a set by using remove() or discard()
#you use pop() to remove a random value as there is no particular order in sets
thisset.remove("strawberry")
print(thisset)
thisset.discard("wildberry")
print(thisset)
thisset.pop()
print(thisset)
#clear()= to clear set and del name_of_set= to delete the set

print("\n")
#join sets
#union() & update() joins 2 sets they will exclude duplicate values
set1= {"a","b","c"}
set2= {1,2,3}
setx = set1.union(set2)
sety = set1|set2
print(setx)
print(sety)
set3= {"John","Elena"}
set4= {"apple","banana","cherry"}
myset= set1|set2|set3|set4
print(myset)
#u can also union set and truple resultant will be a set
y=(7,8,9)
myset2= set1.union(y) #u cant use operand '|' u must use union()
print(myset2)

print("\n")
#intersection '&'
set5= {"apple","banana","cherry",1,0,2}
set6= {"google","microsoft","apple",True,False,2}
#the values True and 1 are considered the same value in sets, and are treated as duplicates
#same goes for False and 0
myset3= set5.intersection(set6)
print(myset3)
myset4= set5 & set6
print(myset4)
set5.intersection_update(set6)
print(set5)

print("\n")
#difference '-' and symmetric difference '^' (they also have difference_update &... func)
#difference only prints non-duplicate values from first set (mentioned)
#symmetric difference prints non-duplicate values from both sets
set7= {"apple","banana","cherry",1,0,2}
set8= {"google","microsoft","apple",True,False,2}
myset5= set7.difference(set8)
print(myset5)
myset6= set7-set8
print(myset6)
myset7= set7.symmetric_difference(set8)
print(myset7)
myset8= set7^set8
print(myset8)

print("\n")
#isdisjoint() to check if sets have intersecting values or not(false= yes; true= no)
myset9= set7.isdisjoint(set8)
print(myset9)