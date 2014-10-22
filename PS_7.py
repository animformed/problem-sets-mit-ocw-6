def fact0(i):
    assert type(i) == int and i >= 0
    if i == 0 or i == 1:
        return 1
    #print i
    print i * fact0(i-1)
    return i * fact0(i-1)
fact0(9)