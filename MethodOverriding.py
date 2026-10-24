class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Bark")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()