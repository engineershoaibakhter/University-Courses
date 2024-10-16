while(True):
    n=int(input('Enter any positive number: '))
    if(n>=1):
        if((n==2)|(n==3)):
            print('Number is prime')
        elif((n==1)):
            print('Number is not prime')
        else:
            if((n%2==0)|(n%3==0)):
                print('Number is not prime')
            else:
                print('Number is prime')
        break
    else:
        print('Number is not +ve')
        continue