# input through a function argument
# check if the input are integers or a sequence, or an empty list
# if the input are set of lists, concatenate them
# return the final concatenation
def adder(*args, **kargs):
    sum = 0
    res = []
    string = ''
    #print args
    #print kargs
    if len(args):
        check = args[0]
        if isinstance(check, int):
            for arg in args:
                sum += arg
            return sum    
        if isinstance(check, list):
            for arg in args:
                for ch in arg:
                    res.append(ch)
            return res
        if isinstance(check, str):
            for arg in args:
                string += arg
            return string
    if kargs:
        res = kargs.values()
        total = res[0]
        for arg in res:
            total += arg
        return res, total
        
 
print(adder(2, 3, 4))
print(adder('spam', 'eggs', 'toast'))
print(adder(['a', 'b'], ['c', 'd'], ['e', 'f'])) 
#print(adder([ ])) 
print(adder(a=1, b=2, c=3))
print(adder(a='aa', b='bb', c='cc'))
        
            
            
        
    
            
            
        
    