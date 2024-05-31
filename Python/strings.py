a= "Hello, World!"
c= " Hello, World! "
print(a[1]) #for individual character

'''Basic Functions'''
print(a.upper())
print(a.lower())
print(len(a))
print(c.strip()) #remove white spaces from end and beginning
print(a.split(','))
print(a.replace('H', 'J')) #replace in string it is case-sensitive


'''Looping through string'''
for x in "banana":
    print(x)

'''String & If statement'''
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)
if "free" in txt:
    print("Term 'free' is present in the text")
if "expensive" not in txt:
    print("Term 'expensive' is not present in the text")

'''Slicing String'''
b= "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
#the last term is not included [2:5]; 2 will be in the output but 5 wont be

'''f strings'''
price= 69.4201
print(f"The price of an onion is {price} dollars")
print(f"The price of an onion is {price:.2f} dollars")
print(f"The price of one tomato is {23*2} dollars")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

"""
ESCAPE CHARACTERS
\"\" Double Quote
txt = "We are the \"Vikings\" from the north." --> We are the "Vikings" from the north.
\'	Single Quote	
    txt = 'It\'s alright.' --> It's alright.
\\	Backslash	
    txt = "This will insert one \\ (backslash)." --> This will insert one \ (backslash).
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	

BOOL NUMBERS
In fact, there are not many values that evaluate to False,
except empty values, such as (), [], {}, "", the number 0, and the value None. 
And of course the value False evaluates to False.
"""

exit()