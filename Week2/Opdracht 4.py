def mybin(number):
    my_string = ''
    assert number >= 0

    if number == 1:
        return '1'
    elif number == 0:
        return my_string + '0'
    elif number%2 == 0:
        number = int(number/2)
        return my_string + mybin(number) + '0'
    else:
        number = int(number/2)
        return my_string + mybin(number) + '1'

for number in range(1,1001):
    if '0b' + mybin(number) != bin(number):
        print('wrong!')
print('Done')

for number in range(-5,1):
    try:
        mybin(i)
        print("Valid binary value")
    except:
        print('Invalid binary value')
