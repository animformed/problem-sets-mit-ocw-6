#L = [1, 2, 4, 8, 16, 32, 64]
#X = 5
#found = False
#i = 0
#while not found and i < len(L):
#    if 2 ** X == L[i]:
#        found = True
#    else:
#        i = i + 1
#        
#if found:
#    print 'at index', i
#else:
#    print X, 'not found'
    
L = []
X = 5
for i in range(0, 7):
    L.append(2 ** i)
print L

if (2 ** X) in L:
    print 'found at index', L.index(2 ** X)
else:
    print 'not found'

