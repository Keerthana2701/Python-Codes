#scope
name = "keer"

def outer():
    name = "vikee"

    def inner():
        name = "aadhvik"
        print("Inner:", name)

    inner()
    print("Outer:", name)

outer()
print("Global:", name)

#closure
#defined inside another function
#has access to parent function's
# variable even afer parent function is executed
#inner function multipler remembers n from 
#outer function
def make_multiplier(n):
    def multiply(x):
        return n * x
    return multiply


var = make_multiplier(7)
print(var(5))
