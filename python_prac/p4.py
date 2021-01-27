class Animal():

    def __init__(self):
        print("ANIMAL CREATED")
    
    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

# 상속
class Dog(Animal):
    
    def __init__(self):
        #Animal.__init__(self)
        print("DOG CREATED")

    # OVERIDE
    def eat(self):
        print("DOG EATING")

#a = Animal()    # ANIMAL CREATED
#a.whoAmI()      # ANIMAL
#a.eat()         # EATING

a = Dog()       # DOG CRAETED
a.whoAmI()      # ANIMAL
a.eat()         # DOG EATING
