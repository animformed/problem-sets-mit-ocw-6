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
   
    