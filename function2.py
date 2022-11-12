num1=10
num2=20


print('function without argument and return value')
def sum():
    sum=num1+num2
    print(sum)
sum()


print('function with argument and without return value')
def sum1(num1,num2):
    sum=num1+num2
    print(sum)
sum1(num1,num2)

print('function with argument and with return value')
def sum2(num1,num2):
    sum=num1+num2
    return sum
value=sum2(num1,num2)
print(value)


print('function without argument and with return value ')

def sum3():
    sum=num1+num2
    return sum
c=sum3()
print(c)
