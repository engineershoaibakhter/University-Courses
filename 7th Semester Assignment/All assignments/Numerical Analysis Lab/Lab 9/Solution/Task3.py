def trapezoidal_rule_with_uneven_segments(data_points):
  n=len(data_points)
  integral=0.0
  for i in range(n-1):
    h=data_points[i+1][0] - data_points[i][0]
    integral+=(1/2)*h*(data_points[i][1]+data_points[i+1][1])
  return integral
datapoints=[(0.0,0.200000),(0.12,1.309729),(0.22,1.305241),(0.32,1.743393),(0.36,2.074903),(0.40,2.456000),(0.44,2.842985),(0.54,3.507297),(0.64,3.181929),(0.70,2.363000),(0.80,0.232000)]
print('Result is ',trapezoidal_rule_with_uneven_segments(datapoints))