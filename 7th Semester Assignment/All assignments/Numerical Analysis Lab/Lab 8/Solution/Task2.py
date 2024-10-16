import math
def function(x):
  return  math.log(x)

def simpson_rule(a,b,n):
  h=(b-a)/n

  x_values=[]
  f_x_values=[]

  i=0

  while i<n:
    x_values.append(a+i*h)
    f_x_values.append(function(x_values[i]))
    i+=1

  result=0
  i=0

  while i<n:
    if i==a or i==b:
      result+=f_x_values[i]

    elif i%2==0:
      result+=2*f_x_values[i]

    else:
      result+=4*f_x_values[i]

    i+=1

  return result*(h/3)
a=math.exp(2)
b=2*math.exp(2)
n=4

print('area under curve: ',simpson_rule(a,b,n))