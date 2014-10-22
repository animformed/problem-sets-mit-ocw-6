class Adder:
    def __init__(self, data=0):
        self.data = data
    def add(self, x, y):
        print 'Not Implemented'
    def __add__(self, other):
        return self.add(self.data, other)
    def __radd__(self, other):
        return self.add(self.data, other)

class ListAdder(Adder):                     # Add two lists       
    def add(self, data, other):
        if isinstance(data, Adder):
            data = data.data
        if isinstance(other, Adder):
            other = other.data
        return data + other
    
class DictAdder(Adder):                     # Add two dictionaries
    def add(self, x, y):
        self.data = x
        other = y
        for item in other:
            if not item in self.data:
                self.data[item] = item
        return self.data
                