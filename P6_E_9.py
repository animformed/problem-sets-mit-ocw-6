class Scene:
    def __init__(self):
        self.cust = Customer()
        self.clk = Clerk()
        self.prt = Parrot()
    def action(self):
        for act in (self.cust, self.clk, self.prt):
            act.line() 
class Customer:
    def line(self):
        print 'IS a buyer'
class Clerk:
    def line(self):
        print 'Manages records'
class Parrot:
    def line(self):
        print 'Eats Chilli'

Scene().action()
        