import math
def function(x,y):
  return -2*y+x**3*math.exp(-2*x)
def rk_4rth_order(x0,y0,x,h):
  n=int((x-x0)/h)
  y=y0
  for i in range(1,n+1):
    k1=h*function(x0,y)
    k2=h*function(x0+(h/2),y+(k1/2))
    k3=h*function(x0+(h/2),y+(k2/2))
    k4=h*function(x0+h,y+k2)
    y=y+(1/6)*(k1+2*k2+2*k3+k4)
  return y
x0=0
y0=1
x=0.1
h=0.1
print('Result: ',rk_4rth_order(x0,y0,x,h))