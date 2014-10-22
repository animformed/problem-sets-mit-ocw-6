def squareRootBi(x, epsilon):
    """
    Assumes x >= 0 and epsilon > 0, return y such that y*y is within (near) epsilon of x
    """
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not ' + str(epsilon)
    
    low = 0
    high = max(x, 1)            # if x is less than 1, since sqrt of 0.25 is 0.5
    guess = (low + high) * 0.5 
    ctr = 1
    while abs(guess ** 2 - x) > epsilon and ctr <= 100:
        print 'low:', low, 'high:', high, 'guess:', guess, 'near ep', guess ** 2 - x
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) * 0.5
        ctr += 1
    assert ctr <= 100, 'iteration count exceeded'
    print 'Bi method. Num. iterations:', ctr, 'Estimate:', guess
    return guess 
        