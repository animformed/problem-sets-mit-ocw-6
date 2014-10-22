class MyError(Exception): pass

def oops():
    raise MyError('spam')
    #raise IndexError

def run():
    try:
        oops()
    except MyError as X:
        print 'oops caught!', X.__class__, X.args[0]
    except IndexError:
        import sys
        print 'IndexError caught', sys.exc_info()[:2]
    else:
        print 'no exception'
        
if __name__ == '__main__':
    run()