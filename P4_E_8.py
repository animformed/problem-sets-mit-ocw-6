#x = y // 2
#while x > 1:
#    if y % x == 0:
#        print (y,'has the factor',x)
#        break
#    x -= 1
#else:
#    print y,'is prime'


def input_num():    
    #import sys
    #global input
    input = raw_input('Enter a number: ')
    try:
        return int(input)
    except: return float(input)

def c_prime():
    num = input_num()
    x = num // 2
    while x > 1:
        if num % x == 0:
            print (str(num) + ' is not a prime')
            break
        x -= 1
    else:
        print (str(num) + ' is a prime')
    c_prime()
                
c_prime()
