__author__ = 'William Bryant'

import math
from abc import ABCMeta, abstractmethod

# Implements the calculations of some properties a shape can have.
class Shape(object):
    """
    Abstract class which implements the necessary code that all shapes have and defines
    the getArea() method which sub-classes must implement.
    """
    __metaclass__ = ABCMeta

    colour = None

    def __init__(self, colour):
        """
        :param colour: Must be a string.
        """
        if type(colour) is not str:
            raise ValueError('The argument colour must be a string')

        self.colour = colour

    def getColour(self):
        return self.colour

    @abstractmethod
    def getArea(self):
        """
        Here child classes of the Shape class must implement the getArea() method
        to calculate the specific area for that type of shape.
        :return: Must return an integer or float - The area based on the type of shape.
        """
        pass


# Implements the calculations of some properties a polygon can have.
class Polygon(Shape):
    """
    Abstract class which defines the getPerimeter() method which sub-classes must implement.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def getPerimeter(self):
        """
        Here child classes of the Polygon class must implement the getPerimeter() method
        to calculate the specific perimeter for that type of polygon.
        :return: Must return an integer or float - The perimeter based on the type of shape.
        """
        pass


# Implements the calculations of some properties a square can have.
class Square(Polygon):
    length = None

    def __init__(self, colour, length):
        """
        :param length: Must be an integer or float
        """
        if type(length) not in [int, float]:
            raise ValueError('The argument length must be an integer or float')
        self.length = length
        super(Square, self).__init__(colour)

    def getArea(self):
        return self.length * self.length

    def getPerimeter(self):
        return 4 * self.length


# Implements the calculations of some properties a circle can have.
class Circle(Shape):
    radius = None

    def __init__(self, colour, radius):
        """
        :param radius: Must be an integer or float
        """
        if type(radius) not in [int, float]:
            raise ValueError('The argument radius must be an integer or float')
        self.radius = radius
        super(Circle, self).__init__(colour)

    def getArea(self):
        return math.pi * (self.radius * self.radius)

    def getCircumference(self):
        """
        Calculates the circumference based on the radius.
        :return: Must return an integer or float - The value of the circumference.
        """
        return 2 * math.pi * self.radius


# Implements the calculations of some properties a rectangle can have.
class Rectangle(Polygon):
    length = None
    width = None

    def __init__(self, colour, length, width):
        """
        :param length: Must be an integer or float
        :param width: Must be an integer or float
        """
        if type(length) not in [int, float]:
            raise ValueError('The argument length must be an integer or float')
        if type(width) not in [int, float]:
            raise ValueError('The argument width must be an integer or float')
        self.length = length
        self.width = width
        super(Rectangle, self).__init__(colour)

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2 * self.length + 2 * self.width


# Testing method for testing and demonstrating.
def test(mySquare=Square("Blue", 2), myRectangle=Rectangle("Yellow", 2, 5), myCircle=Circle("Orange", 6)):
    print("TESTS:")
    print("\nSquare area: ", mySquare.getArea())
    print("Square perimeter: ", mySquare.getPerimeter())
    print("Square colour: ", mySquare.getColour())

    print("\nRectangle area: ", myRectangle.getArea())
    print("Rectangle perimeter: ", myRectangle.getPerimeter())
    print("Rectangle colour: ", myRectangle.getColour())

    print("\nCircle area: ", myCircle.getArea())
    print("Circle circumference: ", myCircle.getCircumference())
    print("Circle colour: ", myCircle.getColour())


# test()
# test(mySquare=Square(input("Colour:"),  int(input("Length"))))


def askMultichoiceQuestion(question, options):
    while True:
        print("\n" + question)
        optionNumber = 1
        for option in options:
            print("\n(" + str(optionNumber) + ") " + option)
            optionNumber += 1
        amount = len(options)
        try:
            index = int(input("> ")) - 1
            if index not in range(amount):
                raise ValueError()
            return options[index]
        except ValueError:
            print("You need to enter numbers 1 to", amount)


# Check if integer input is appropriate for a unit above 0.
def tryIntInput(name, question):
    while True:
        try:
            value = int(input(question))
            if value <= 0:
                raise ValueError(name + " below 1")
            return value
        except ValueError:
            print("That is not an possible " + name)


def start():
    shapeType = askMultichoiceQuestion("What type of shape would you like to use for calculations?",
                                       ["Polygon", "Circle"])
    if shapeType == "Polygon":
        polygonType = askMultichoiceQuestion("What type of polygon would you like to use for the calculations?",
                                             ["Square", "Rectangle"])
        polygon = None
        colour = input("What colour is it?\n> ")
        length = tryIntInput("length", "What is the length?\n> ")
        if polygonType == "Square":
            polygon = Square(colour, length)
        elif polygonType == "Rectangle":
            width = tryIntInput("length", "What is the height?\n> ")
            polygon = Rectangle(colour, length, width)
        whatToGet = askMultichoiceQuestion("What do you want to get?", ["Area", "Perimeter", "Colour"])
        if whatToGet == "Area":
            print("Area: ", polygon.getArea())
        elif whatToGet == "Perimeter":
            print("Perimeter: ", polygon.getPerimeter())
        elif whatToGet == "Colour":
            print("Colour: ", polygon.getColour())
    elif shapeType == "Circle":
        colour = input("What colour is your circle?\n> ")
        radius = tryIntInput("radius", "What is the radius of your circle?\n> ")
        circle = Circle(colour, radius)
        whatToGet = askMultichoiceQuestion("What do you want to get?", ["Area", "Circumference", "Colour"])
        if whatToGet == "Area":
            print("Area: ", circle.getArea())
        elif whatToGet == "Circumference":
            print("Circumference: ", circle.getCircumference())
        elif whatToGet == "Colour":
            print("Colour: ", circle.getColour())
    print("You can create more shapes now:")
    start()


def init():
    print("+++===WELCOME TO SHAPE MAKER/CALCULATOR - BY WILLIAM BRYANT===+++")
    start()

if __name__ == '__main__':
    init()
