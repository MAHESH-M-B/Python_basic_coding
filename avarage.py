num1=int(input('enter the first number'))
num2=int(input('enter the second number'))
num3=int(input('enter the third number'))

average=(num1+num2+num3)/3

print('the average is ',average)



# using function

def average(num1,num2,num3):
    average=(num1+num2+num3)/3
    return average
num1=int(input('enter the first number'))
num2=int(input('enter the second number'))
num3=int(input('enter the third number'))
c=average(num1,num2,num3)
print(c)