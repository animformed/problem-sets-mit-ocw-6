def search(s, e):
    answer = None
    i = 0
    nonCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print answer, numCompares
    
def bsearch(s, e, first, last):
    print first, last
    if(last - first) < 2:                       # if the length of the list is less than 2
        return s[first] == e or s[last] == e    # check if item exists in the first and last element
    mid = first + (last - first)/2              # get the length between first and last and divide by half to get mid
    if s[mid] == e:
        return True
    if s[mid] > e:                              # if item is greater the mid
        return bsearch(s, e, first, mid-1)      # make the previous value before mid as the last, and keep the first
    return bsearch(s, e, mid + 1, last)


    