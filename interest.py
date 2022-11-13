p=input('enter the principle amount')
n=input('enter the  number of years')
r=input('enter the interest rate')
si=(int(p)*int(n)*int(r))/100
print('the interest is ',si)

# using function
def simple_interest():
    p=int(input('enter the principle amount'))
    n=int(input('enter the no of years'))
    r=int(input('enter the principle amount'))
    si=(p*n*r)/100
    return si
print(simple_interest())