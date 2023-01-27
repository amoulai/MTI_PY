import sys


class Shape:
    def draw(self):
        print("Shape.draw")

    def erase(self):
        print("Shape.erase")


class Circle(Shape):
    def draw(self):
        print("Circle.draw")

    def erase(self):
        print("Circle.erase")


class Square(Shape):
    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")


class Triangle(Shape):
    def draw(self):
        print("Triangle.draw")

    def erase(self):
        print("Triangle.erase")


class Rectangle(Shape):
    def draw(self):
        print("Rectangle.draw")

    def erase(self):
        print("Rectangle.erase")


if __name__ == "__main__":
    for type in ("Circle", "Square", "Triangle", "Rectangle"):
        if type == "Circle":
            shape = Circle()
        elif type == "Square":
            shape = Square()
        elif type == "Triangle":
            shape = Triangle()
        elif type == "Rectangle":
            shape = Rectangle()
        else:
            print("Bad shape creation: " + type)
            sys.exit()
        shape.draw()
        shape.erase()
