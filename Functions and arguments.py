print('functions and arguments')
def addition(a,b):
    return a+b
print(addition(4,6))

#when you are not sure how many arguments
# will be passed
def addition1(*nos):
    return sum(nos)
print(addition1(2,5,6,7,8,8,8,9))

#recursive function
print('recursive function')
def factorial(n):
    if n==0:
     return 1
    else:
     return n* factorial(n-1)

print(factorial(5))

