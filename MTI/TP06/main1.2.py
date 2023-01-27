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


class Circle2D(Circle):
    def draw(self):
        print("Circle2D.draw")

    def erase(self):
        print("Circle2D.erase")


class Circle3D(Circle):
    def draw(self):
        print("Circle3D.draw")

    def erase(self):
        print("Circle3D.erase")


class Square(Shape):
    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")


class Square2D(Square):
    def draw(self):
        print("Square2D.draw")

    def erase(self):
        print("Square2D.erase")


class Square3D(Square):
    def draw(self):
        print("Square3D.draw")

    def erase(self):
        print("Square3D.erase")


class ShapeFactory:
    @staticmethod
    def createShape(type):
        if type == "Circle":
            return Circle()
        elif type == "Square":
            return Square()
        else:
            print("Bad shape creation: " + type)
            sys.exit()


class ShapeFactory2D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type == "Circle2D":
            return Circle2D()
        elif type == "Square2D":
            return Square2D()
        else:
            print("Bad shape creation: " + type)
            sys.exit()


class ShapeFactory3D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type == "Circle3D":
            return Circle3D()
        elif type == "Square3D":
            return Square3D()
        else:
            print("Bad shape creation: " + type)
            sys.exit()


if __name__ == "__main__":
    for type in ("Circle2D", "Square2D"):
        shape = ShapeFactory2D.createShape(type)
        shape.draw()
        shape.erase()
    for type in ("Circle3D", "Square3D"):
        shape = ShapeFactory3D.createShape(type)
        shape.draw()
        shape.erase()
