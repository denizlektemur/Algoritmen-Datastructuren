def mybin(n):
    my_string = ''
    assert n>= 0

    if n == 1:
        return '1'
    elif n == 0:
        return my_string + '0'
    elif n%2 == 0:
        n = int(n/2)
        return my_string + mybin(n) + '0'
    else:
        n = int(n/2)
        return my_string + mybin(n) + '1'

for i in range(1,1001):
    if '0b' + mybin(i) != bin(i):
        print('wrong!')
print('Done')

for i in range(-5,1):
    try:
        mybin(i)
        print("Valid binary value")
    except:
        print('Invalid binary value')
