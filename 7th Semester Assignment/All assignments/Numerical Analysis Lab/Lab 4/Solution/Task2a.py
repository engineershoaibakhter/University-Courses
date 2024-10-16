import math
def f(x):
  return math.cos(x)-3*x+1

def g(x):
  return (math.cos(x)+1)/3

def fixed_point_iterative_method(x0,iterations):
  step=1
  x1=g(x0)
  while(step<iterations):
    x0=x1
    x1=g(x0)
    step+=1
  print(f'approx root: {x1:.3f}')
x0=1.0
iterations=50
fixed_point_iterative_method(x0,iterations)