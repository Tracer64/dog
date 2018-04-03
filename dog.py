class Pet:
    """ This is the beginning of a class for a Pet """
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

class Dog(Pet):
    """ Dog inherits from Pet """

d = Dog('Fluffy')

def speak("Dog")
d.speak("Fluffy")
print("Woof")

d.add_weight(12)
print(d.weight)
    
class Cat(Pet):
    """ Cat inherits from Pet """
    
c = ("Tiger")

def speak("Cat")
c.speak("Tiger")
print("Meow")

c.add_weight(8)
print(d.weight)
