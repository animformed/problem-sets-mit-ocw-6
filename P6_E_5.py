class MySet:
    def union(self, *args):
        res = []
        for mem in args:
            for item in mem:
                if not item in res:
                    res.append(item)
        return set(res)
    def intersection(self, *args):
        res = []
        #print res
        for item in args[0]:
            #print item
            for next in args[1:]:
                #print next
                if item not in next: break   # if break, control passes on to the previous for loop
            else:                                   # else only if it doesn't hit break
                res.append(item)
        return set(res)
                
                
                
        