class Meta:
    def __getattr__(self, other):
        print 'getattr: {0}'.format(other)
        #return getattr(self, other)
    def __setattr__(self, other, value):
        print 'setattr: {0}, {1}'.format(other, value)
        #return setattr(self, other, value)