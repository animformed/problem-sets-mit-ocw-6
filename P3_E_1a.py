S = raw_input('Enter a string: ')   # only alpha-numeric here
if not S.isdigit():
    for x in S:
        c = ord(x)
        print('The ASCII code of ' + str(x) + ' is: ' + str(c))
else:
    print('Wrong Input')
    
