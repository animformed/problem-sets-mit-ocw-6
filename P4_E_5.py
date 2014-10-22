# input a keyword based entry, store as a dictionary, and then find
# the sum of key values.
def copyDict(**kargs):
    print kargs
    newDict = {}
    for (key, value) in kargs.items():
        newDict[key] = value
    return newDict

copyDict(name = 'Bob', age = 45, job = 'dev')