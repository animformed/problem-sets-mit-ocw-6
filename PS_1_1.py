# To calculate and print the 1000th prime number

input = 3       # state variables. You can also input these via raw_input() or sys.argv from command line
count = 1
while (input):
    for check in range(2, ((input//2)+1)):
        if(check):
            if input % check == 0:
                break
    else:
        count += 1
    if count == 1000:
        print 'The 1000th prime is: ' + str(input)
        break
    input += 1
            