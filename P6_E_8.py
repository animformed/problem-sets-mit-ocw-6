class Animal:
    def speak(self):
        print 'Animal'
    def reply(self):
        self.speak()
class Mammal(Animal):
    def speak(self):
        print 'Mammal'
class Cat(Mammal):
    def speak(self):
        print 'Cat'
class Dog(Mammal):
    def speak(self):
        print 'Cat'
class Primate(Mammal):
    def speak(self):
        print 'Primate'
class Hacker(Primate):
    pass

spot = Cat()
spot.reply()
data = Hacker()
data.reply()