class Pet:
    """ This is the beginning of a class for a Pet """
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

class Dog(Pet):
    """ Dog inherits from Pet """


class Cat(Pet):
    """ Dog inherits from Pet """

c = Dog('Fluffy')
c.add_weight(12)
print(c.weight)

# c.name = "Fluffy"

# x = Cat('Spike')
# x.name = "Spike"

# x.add_weight(12)
# x.add_wieght(12)

print(c.name)

# print(x.name)
# print(x.weight)
