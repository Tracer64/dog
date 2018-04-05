class Pet:
    """ This is the beginning of a class for a Pet """
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

class Dog(Pet):
    """ Dog inherits from Pet """
    def speak(self):
            """ I moved the speak function you
                tried to create below
                to inside the dog class """
            return "bark"
    
class Cat(Pet):
    """ Cat inherits from Pet """
    def speak(self, voice="meow"):
        """ The cat version of the speak method has a parameter voice
            with a default value of 'meow'.
            If no voice argument is passed to Cat.speak()
            it will use the default value of meow """
        self.voice = voice
        return self.voice

d = Dog('Fluffy')
print(d.speak())

d.add_weight(12)
print(d.weight)

c = Cat("Tiger")


print(c.speak())
print(c.speak('purrrrrr'))

c.add_weight(8)
print(c.weight)
