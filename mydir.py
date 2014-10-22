"""
mydir.py: a module that lists the namespaces of other modules
"""

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
        #import print30
        sepline = sepchr * seplen
        if verbose:
                print sepline 
                print('name:' + str(module.__name__) + ' file:' + str(module.__file__))
                print sepline 
        count = 0
        for attr in module.__dict__.keys():
                print('{0}) {1}'.format(count, attr)),
                if attr.startswith(' '):
                        print '<buit-in name>'
                else:
                        print(getattr(module, attr))
                count += 1
        if verbose:
                print sepline
                print(module.__name__, 'has {0} names'.format(count))
                print sepline
if __name__ == '__main__':
        import mydir
        listing(mydir)