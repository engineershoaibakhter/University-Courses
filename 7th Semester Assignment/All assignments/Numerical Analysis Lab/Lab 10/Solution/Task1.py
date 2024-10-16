import math
def function(x,y):
  return 2-math.exp(-4*x)-2*y
def eulers_method(t0,tn,y0,h):
  while(t0<tn):
    y0+=h*function(t0,y0)
    t0+=h
  print('Approx solution: ',y0)
t0=0
y0=1
h=0.1
tn=[0.1,0.2,0.3,0.4,0.5]
for i in range(0,(len(tn))):
  eulers_method(t0,tn[i],y0,h)