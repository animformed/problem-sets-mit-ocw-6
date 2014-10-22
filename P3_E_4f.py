L = [pow(2, x) for x in range(7)]
X = 5
#for i in range(0, 7):
#    L.append(2 ** i)
print L

if (2 ** X) in L:
    print 'found at index', L.index(2 ** X)
else:
    print 'not found'
