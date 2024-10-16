import math

def function(x):
  return 0.5-x*math.exp(-x**2)+2*x

def golden_section_search_for_max(function,a,b,tolerance=1e-5):
  phi=(1+5**1/2)/2

  while abs(b-a)>tolerance:
    x1=b-(b-a)/phi
    x2=a+(b-a)/phi

    if function(x1)>function(x2):
      b=x2
    else:
      a=x1
  return (a+b)/2

def golden_section_search_for_min(function, a, b, tolerance=1e-5):
    phi = (1 + math.sqrt(5)) / 2
    while abs(b - a) > tolerance:
        x1 = b-(b - a)/phi
        x2 = a + (b - a)/phi
        if function(x1) < function(x2):
            b=x2
        else:
            a = x1

    return (a + b)/ 2

a=0
b=2
print('Golden Section Search for Minimum: ', golden_section_search_for_min(function,a,b,tolerance=1e-5))
print('Golden Section Search for Maximum: ', golden_section_search_for_max(function,a,b,tolerance=1e-5))