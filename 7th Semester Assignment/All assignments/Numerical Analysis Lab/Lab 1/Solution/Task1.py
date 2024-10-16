import cmath
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))
D=(b*b)-(4*a*c)
x1=(-b+cmath.sqrt(D))/(2*a)
x2=(-b-cmath.sqrt(D))/(2*a)
print('x1: ',x1)
print('x2: ',x2)