D1 = {'job': 'dev', 'age': 45, 'name': 'Bob'}
D2 = {'job': 'mgr', 'age': 35, 'name': 'Hans'}

def addDict(d1, d2):
    print d1, d2
    d1.update(d2)
    #sorted(d1)
    print d1
    return d1

D = addDict(D1, D2)
print D