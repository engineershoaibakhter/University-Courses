def function(x,y):
  return (x-y)/2
def rk_2nd_order(x0,y0,x,h):
  n=int((x-x0)/h)
  y=y0
  for i in range(1,n+1):
    k1=h*function(x0,y)
    k2=h*function(x0+h,y0+k1)
    y=y+(1/2)*(k1+k2)
  return y
x0=0
y0=1
x=0.2
h=0.1
print('Result: ',rk_2nd_order(x0,y0,x,h))