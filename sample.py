# values=['mahesh','mukesh','maneesh']

# print(values[1])
# print(values[0:2])

# values=values+['1','2','3']
# print(values)


# b=100
# values.append(b)

# print(values)




x='global x'


def test():
    global x
    x='local x'
    print(x)

test()
print(x)