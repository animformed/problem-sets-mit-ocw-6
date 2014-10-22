class MyError(Exception): pass

def safe(func, *args):
    try:
        func(*args)
    except Exception:
        import sys
        print 'Exception raised', sys.exc_info()[:2]

def oops():
    raise MyError('spam')

safe(oops)    


    