def print_max(x, y):
    '''Print the max of the two number

    the two numbers should be integer.
    '''

    x = int(x)
    y = int(y)
    if x>y:
        print(x,'is the max.')
    elif x<y:
        print(y,'is the max.')
    else:
        print(x,y,'is the same.')

print_max(3,5)
print(print_max.__doc__)
help(print_max)
