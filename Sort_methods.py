def bubbleSort(L):
    check = True
    while check:
        check = False
        for j in range(len(L)):
            for i in range(len(L)-1):
                if L[i] > L[i+1]:
                    temp = L[i]
                    L[i] = L[i+1]
                    L[i+1] = temp
                    check = True
    return L
            
def selectionSort(L):
    for i in range(len(L)-1):
        minIndex = i
        for j in range(i+1, len(L)):
            if L[j] < L[minIndex]:
                minIndex = j
        if minIndex != i:
            tmp = L[i]
            L[i] = L[minIndex]
            L[minIndex] = tmp
    return L
            
def mergeMain(left, right):
    """
    Assumes left and right are sorted lists. Returns a new sorted list containing the 
    same elements as (left + right) would contain.
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):     # runs until one of the sides gets empty
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):                    # only one of these while pieces will be called, since it'd be left
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
    
def mergeSort(L):
    """
    Returns a new sort list containing the same elements as L.
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) / 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        together = mergeMain(left, right)
        print 'merged', together
        return together
    
Li = selectionSort([1, 4, 3, 6, 5, 2, 8, 7, 45, 53, 76, 4, 78, 2, 6, 24, 65, 7, 3, 6, 9, 4, 75, 34, 53, 5, 6, 34, 5, 7, 75, 6, 3, 34, 67, 3, 6, 34, 34, 75, 6, 6, 86, 6, 45, 8, 2, 4, 5])
print Li
# hashing
#-----------
# the idea of a hash function is to map any kind of data into integers
def create(smallest, largest):
    intSet = []
    for i in range(smallest, largest + 1):
        intSet.append(None)
        return intSet
    
def insert(intSet, e):          # insert values to create sets. Marks 1 in each of those spots
    intSet[e] = 1

def member(intSet, e):
    return intSet[e] == 1

