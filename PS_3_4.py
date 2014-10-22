"""
This function takes two arguments: a target string and a key string. It returns a tuple of all
starting points of matches of the key to the target, such that at exactly one element of the 
key is incorrectly matched to the target.
"""
def subStringMatchExactlyOneSub(key, target):
    
    k_sub = []
    cmp = []
    res = []
    pos = 0
    
    result_t = []
    
    for sub in range(len(key)):             
        tmp = key[:sub] + ' ' + key[sub+1:]
        k_sub.append(tmp)
    
    print k_sub
    
    while len(target)>(len(key)-1):
        temp = target[:len(key)]
        cmp.append(temp)
        target = target[1:] 
        
    print list(enumerate(cmp)) 
        
    for item in k_sub:
        pos = 0                         # to record the index of matching string subset
        tmp_res = []
        for strg in cmp:
            count = 0
            for i in range(len(key)):
                if item[i] == strg[i]:
                    count += 1
                
            if count == (len(key)-1):
                tmp_res.append(pos)
            pos += 1
        res.append(tmp_res)
        
    print 'Individual matching positions:',res
    
    for item in res:                    # storing the result
        for x in item:
            if x not in result_t:
                result_t.append(x)
                
    result_t.sort()
    return tuple(result_t)
    
if __name__ == '__main__':    
    target_c = 'atgacatgcacaagtatgcat'
    key_c = 'atgc'
    ct = subStringMatchExactlyOneSub(key_c, target_c)
    print ct
    
    
    
    