def simpson_three_eight_rule_with_datapoints(datapoints):
  n=len(datapoints)-1
  h=datapoints[1][0]-datapoints[0][0]
  integral=datapoints[0][1]+datapoints[-1][-1]
  for i in range(1,n):
    if i%3==0:
      integral+=2*datapoints[i][1]
    else:
      integral+=3*datapoints[i][1]
  return integral*(3*h/8)
datapoints=[(1.4,4.0552),(1.6,4.953),(1.8,6.0436),(2,7.3891),(2.2,9.025),(2.4,10.092),(2.6,11.099)]
print('Result is ',simpson_three_eight_rule_with_datapoints(datapoints))