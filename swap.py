a=10
b=20
c=20
d=30
temp=a
a=b
b=temp
print(a)
print(b)

def swap(c,d):
    temp=c
    c=d
    d=temp
    print(c)
    print(d)

swap(c,d)