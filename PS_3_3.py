def subStringMatchExact(target, key, count = 0):
    import sys
    if len(key) > len(target):
        print 'Target is shorter than key. Quitting!'
        sys.exit(40)
        
    lt = len(key)
    count = 0
    pos = ()                # to record positions
    
    while(len(target) > len(key)):
        st = target[slice(None, lt)]
        
        if st == key:
            pos += ((count,))
        target = target[1:]
        count += 1
    return pos

def constrainedMatchPair(st_a, st_b, len_a):
    res = ()
    for start1 in st_a:
        for start2 in st_b:
            if (start1 + len_a + 1) == start2:
                res += (start1, start2,)
    return res
                
                
def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        #print match1, match2
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

if __name__ == '__main__':    
    target_c = 'atgacatgcacaagtatgcat'
    print 'printing target by index'
    print list(enumerate(target_c))
    key_c = 'atgc'
    subStringMatchOneSub(key_c, target_c)
#    print 'The Match Positions (subStringMatchExact):', ct     
    