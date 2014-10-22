def oops():
    raise IndexError

def run():
    try:
        oops()
    except IndexError:
        print 'oops caught!'
    else:
        print 'no exception'
        
if __name__ == '__main__':
    print __name__
    run()