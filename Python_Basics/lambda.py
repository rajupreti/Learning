"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""
x= lambda a: a+10
print(x(5))
x= lambda a,b: a*b
print(x(5,2))

print("\n")
# Power of lambda is when u use them as an anonymous function inside another function
def power(n):
    return lambda f: n*f
x = power(5)
print(x(2))