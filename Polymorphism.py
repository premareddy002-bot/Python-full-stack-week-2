class Circle:
    def area(self):
        radius = float(input("Enter circle radius: "))
        print("Area of Circle:", 3.14 * radius * radius)


class Rectangle:
    def area(self):
        length = float(input("Enter rectangle length: "))
        breadth = float(input("Enter rectangle breadth: "))
        print("Area of Rectangle:", length * breadth)


c = Circle()
r = Rectangle()

c.area()
r.area()