L = [2, 4, 9, 16, 25]

def f_loop(Ls):
    res = []
    from math import sqrt
    for x in Ls:
        res.append(sqrt(x))
    return res

def f_map(Ls):
    from math import sqrt
    return map(sqrt, Ls)

def f_Lcmp(Ls):
    from math import sqrt
    return [sqrt(x) for x in Ls]

print(f_loop(L))
print(f_map(L))
print(f_Lcmp(L))

import sys, time
reps = 1000000
repslist = range(reps)

def timer(func, Ls):
    start = time.clock()
    for itr in repslist:
        ret = func(Ls)
    elapsed = time.clock() - start
    return (elapsed, ret)
    
print('\n' + sys.version)
for tester in (f_loop, f_map, f_Lcmp):
    elapsed, result = timer(tester, L)
    print '-' * 43
    print ('{0:<9}: {1:.5f} => [{2}...{3}]'.format(tester.__name__, elapsed, result[0], result[-1]))
    
    