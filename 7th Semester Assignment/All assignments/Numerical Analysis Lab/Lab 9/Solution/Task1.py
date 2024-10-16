def function(x):
  return (1/2)+25*x-200*x**2+675*x**3-900*x**4+400*x**5
def simpson_three_eight_rule(a,b,n):
  h=(b-a)/n
  sum=function(a)+function(b)
  for i in range(1,n):
    if i%3==0:
      sum+=2*function(a+i*h)
    else:
      sum+=3*function(a+i*h)
  return sum *(3*h/8)
a=0
b=0.8
n=3
print(simpson_three_eight_rule(a,b,n))