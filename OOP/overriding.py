class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):              # override method of parent
        print("This Rabbit is eating")

rabbit = Rabbit()
rabbit.eat()