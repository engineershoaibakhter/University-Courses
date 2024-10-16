def factorial(n):
  if(n<=1):
    return 1
  else:
    return n*factorial(n-1)
  

while(True):
  n=int(input('Enter number: '))
  if(n<0):
    print('Please Enter +ve Number')

  else:
    break
print(factorial(n))