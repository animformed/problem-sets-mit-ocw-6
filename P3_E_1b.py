S = raw_input('Enter a string: ')   # only alpha-numeric here
sum = 0
if not S.isdigit():
    for x in S:
        c = ord(x)
        print('The ASCII code of ' + str(x) + ' is: ' + str(c))
        sum += c
    print('The sum of ASCII codes: ' + str(sum))
elif S.isdigit():
    print('Wrong Input')
    
    