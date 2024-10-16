import math
def f(x):
  return 2*x**3-7*x**2-6*x+1

def g(x):
  return ((7*x**2+6*x-1)/2)**(1/3)

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