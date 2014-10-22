import math, decimal      

def calculate(l_num):
    """
    This function computes the sum of the logarithms of all the primes from 2 to an input number,
    and returns the sum of the logs of the primes and the ratio of these two quantities.
    """
    input_l = int(l_num)            # this input is local to def according to LEGB scope rule
    sum = decimal.Decimal('0.0')
    input = 3                       # staring from 3, since 1 is already a prime
    while (input < input_l):
        for check in range(2, ((input//2)+1)):      # floor division (input//2); check new rules for python 3.x
            if(check):
                if input % check == 0:
                    break
        else:
            sum += decimal.Decimal(str(math.log(input)))          
        input += 1
    if(input > 3):
        ratio = decimal.Decimal(str(sum)) / decimal.Decimal(str(input_l))
    return sum, ratio

if __name__ == '__main__':
    inp = raw_input("Enter a large number: ")
    p_sum, p_ratio = calculate(inp)
    print 'The sum of log() of all primes less than {0}: {1}'.format(inp, p_sum)
    print 'The ratio of sum of ln of primes and the input number: ' + str(p_ratio)


            