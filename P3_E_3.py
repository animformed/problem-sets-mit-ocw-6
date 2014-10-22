D = dict(name = 'Bob', age = 45, job=('mgr', 'dev'))
for key in sorted(D.keys()):
    print D[key],

D = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
keys  = D.keys()
keys.sort()
print '\n'
for key in keys:
    print D[key],

