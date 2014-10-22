"""
This function takes two arguments: a target string, and a key string. It should return a tuple of 
the starting points of matches of the key string in the target string, when indexing starts at 0.
"""
def subStringMatchExact(target, key, count = 0):
    
    lt = len(key)
    count = 0
    pos = ()                # to record positions
    
    while(len(target) > (len(key)-1)):
        st = target[slice(None, lt)]
        
        if st == key:
            pos += ((count,))
        target = target[1:]
        count += 1
    return pos

if __name__ == '__main__':    
    target_c = 'atgacatgcacaagtatgcat'
    key_c = 'atgc'
    ct = subStringMatchExact(target_c, key_c)
    print 'The Match Positions (subStringMatchExact):', ct