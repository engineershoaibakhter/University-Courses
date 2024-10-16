import math
def arcTan(x,N):
    res=0.0
    for i in range(N):
        n=(((-1)**i)*(x**((2*i)+1)))/((2*i)+1)
        res+=n
    
    return res

print('Actual PI: ',math.pi)
terms=100
approx_pi=4*arcTan(1,terms)
print('Approximate Value of PI: ',approx_pi)
truncationError=abs(approx_pi-math.pi)
print('Truncation Error: ',truncationError)