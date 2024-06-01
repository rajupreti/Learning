''' if loop    '''
a= 20
b= 30
c= 40
#method 1
if a<b and c>b:
    print(f"B= {b} is only greater than A= {a}")
elif a>b and c>a:
    pass
else:
    print("Condition is not True")

#method 2
print(f"B= {b} is only greater than A= {a}") if a<b and c>b else print("") if a>b and c>a else print("Condition is not True")

print("\n")
''' while loop   '''
#used while...else loop (different from if else)
number= input("Enter a number between 0-9: ")
number= int(number)
if number>= 0 and number<= 9:
    while number<10:
        print(number)
        number+=1
    else:
        print("Thank You!")

print("\n")
#u can use break and continue (breaks exits the loop; continue stops the current and continue with next)
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("\n")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("\n")
''' for loop    '''