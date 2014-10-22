class Employee:
    def takeOrder(self, foodName):              # Return a Food, with requested name
        return Food(foodName)
class Food:
    def __init__(self, food):                     # Store food name
        self.food = food
class Customer:
    #def __init__(self):                                 # Initialize my food to None
    
    def placeOrder(self, foodName, employee):           # Place order with an Employee
        self.food = employee.takeOrder(foodName)
        #Food.__init__(self.food)
    def printFood(self):                                # Print the name of my food
        print 'Food: {0}'.format(self.food.food)
class Lunch:
    def __init__(self):                         # Make/embed Customer and Employee
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):                  # Start a Customer order simulation
        self.customer.placeOrder(foodName, self.employee)
    def result(self):                           # Ask the Customer what Food it has   
        self.customer.printFood()
        
x = Lunch()
x.order('burritos')
x.result()
x.order('pizza')
x.result()