import math
def func(x):
    return math.cos(x)-x*math.exp(x)

def derivFunc(x):
    return -x*math.exp(x)-math.exp(x)-math.sin(x)

def newtonRaphson(x):
    prev_x = float('inf')
    
    while x != prev_x:
        prev_x = x
        x = x - (func(x) / derivFunc(x))
    
    print("The approximate root value is:", "%.4f" % x)

initial_guess = 1
newtonRaphson(initial_guess)
