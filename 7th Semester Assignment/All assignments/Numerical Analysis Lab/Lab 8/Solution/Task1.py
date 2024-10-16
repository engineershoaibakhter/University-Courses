import math
def function(x):
  return math.exp(x)

def trapeziodal_rule(a,b,n):
  h=(b-a)/n
  result= function(a)+function(b)

  i=1

  while i<n:
    result+=2*function(a+i*h)
    i+=1
  return result*(h/2)
a=0
b=2
n=2
print('area under the curve : ',trapeziodal_rule(a,b,n))