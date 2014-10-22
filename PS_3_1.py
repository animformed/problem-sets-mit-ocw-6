"""
Two functions, called, countSubStringMatch and countSubStringMatchRecursive that take two arguments,
a key string and a target string. These functions iteratively and recursively count the number of 
instances of the key in the target string.
"""
def countSubStringMatch(target, key):   
           
    lt = len(key)
    count = 0
    
    while(len(target) > (len(key)-1)):
        st = target[slice(None, lt)]
        
        if st == key:
            count += 1
        target = target[1:]
        
    return count

def countSubStringMatchRecursive(target, key):
    
    lt = len(key)
    count = 0
    
    if(len(target) > (len(key)-1)):          # to not to skip the last len sized group
        st = target[slice(None, lt)]
        if st == key:
            count += 1
        count += countSubStringMatchRecursive(target[1:], key)
    return count
        
        
if __name__ == '__main__':    
    target_c = 'atgacatgcacaagtatgcat'
    key_c = 'atgc'
    ct = countSubStringMatch(target_c, key_c)
    print 'The Count is (countSubStringMatch):', ct
    ct = countSubStringMatchRecursive(target_c, key_c)
    print 'The Count is (countSubStringMatchRecursive):', ct