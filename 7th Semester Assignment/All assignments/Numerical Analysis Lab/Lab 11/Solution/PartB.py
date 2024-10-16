def function(x,y):
  return 1-y*y*y
def rk_3rd_order(x0,y0,x,h):
  n=int((x-x0)/h)
  y=y0
  for i in range(1,n+1):
    k1=h*function(x0,y)
    k2=h*function(x0+(h/2),y+(k1/2))
    k3=h*function(x0+h,y0+2*k2-k1)
    y=y+(1/6)*(k1+4*k2+k3)
  return y
x0=0
y0=0
x=0.3
h=0.1
print('Result: ',rk_3rd_order(x0,y0,x,h))