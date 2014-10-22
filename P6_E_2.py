class MyList:
    def __init__(self, mlist = []):   # The input is copied with append because, the input may not be a list, and it is mutable
        print 'init'
        self.mylist = []
        self.appendList(mlist)
    def appendList(self, input):
        print 'ap_list'
        for x in input:
            if not x in self.mylist:
                self.mylist.append(x)
    def __add__(self, input):
        print '__add__'
        if isinstance(input, MyList):
            input = input.mylist
        return MyList(self.mylist + input)
    def __mul__(self, input):
        print '__mul__'
        return MyList(self.mylist * input)
    def __getitem__(self, index):
        print '__getitem__'
        return self.mylist[index]
    def __len__(self):
        print '__len__'
        return len(self.mylist)
    def __getslice__(self, start, end):
        print '__getslice__'
        return MyList(self.mylist[start:end])
    def __getattr__(self, value):
        print '__getattr__'
        return getattr(self.mylist, value)
    def __repr__(self):
        print '__repr__'
        return repr(self.mylist)
    def append(self, input):
        print 'append'
        return self.mylist.append(input)
    
     
                
        
    