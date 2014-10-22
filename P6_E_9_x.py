class Message:
    def line(self):
        print '{0}: {1}'.format(self.__class__.__name__, repr(self.action()))
class Scene:
    def __init__(self):
        self.cust = Customer()
        self.clk = Clerk()
        self.prt = Parrot()
    def action(self):
        for act in (self.cust, self.clk, self.prt):
            act.line() 
class Customer(Message):
    #name = 'Customer'
    def action(self):
        return "that's one ex-bird!" 
class Clerk(Message):
    #name = 'Clerk'
    def action(self):
        return "no it isn't..."
class Parrot(Message):
    #name = 'Parrot'
    def action(self):
        return None

Scene().action()