# LSP(Liskov Substitution Principle) - parent class should always be able to
# substitute child class without altering the behaviour.

"""

Code Violating LSP

"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, w):
        self.width = w
        self.height = w

    def set_height(self, h):
        self.width = h
        self.height = h


def resize_shape(shape: Rectangle):
    shape.set_width(10)
    shape.set_height(5)
    assert shape.area() == 50


resize_shape(Rectangle(5, 10))  # works
resize_shape(Square(5))  # gives error

"""

LSP Complaint Code 

"""


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def test_area(shape: Shape, expected):
    actual = shape.area()
    assert actual == expected, f"Expected {expected}, got {actual}"


test_area(Square(5), 25)
test_area(Rectangle(5, 5), 25)
