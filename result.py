mark1=int(input('enter your mark'))
if mark1 >= 50:
    print('passed')
else:
    print('failed')


# using function
def pass_failed(mark):
    if mark >= 50:
        print('passed')
    else:
        print('failed')
    return(mark)

mark2=int(input('enter the mark you got'))
pass_failed(mark2)
