import math
def function(x,y):
  return -(1/2)*math.exp(x/2)*math.sin(5*x)+5*math.exp(x/2)*math.cos(5*x)+y

def predictor_corrector_method(t0,tn,y0,h):
  while(t0<tn):
    t1=t0+h
    p_y=y0+h*function(t0,y0)
    c_y=y0+(h/2)*(function(t0,y0)+function(t1,p_y))
    t0=t1
    y0=p_y
  return y0
t0=0
y0=0
h=[0.1,0.05,0.01,0.005,0.001]
tn=[1,2,3,4,5]
for i in range(0,(len(tn))):
  print('At tn:',tn[i])
  for j in range(0,len(h)):
    print('Approx Solution at',h[j],':',predictor_corrector_method(t0,tn[i],y0,h[j]))

  print('\n')