# This is a sample Python script.
import math
from stringprep import b1_set


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        area = math.pi * self.r ** 2
        return area

    def perimeter(self):
        per = 2 * math.pi * self.r
        return per

    def __str__(self):
        return "Area of the circle is: " + str(self.area()) + " and the perimeter of the circle is: " + str(
            self.perimeter())


class Rectangle(Shape):
    def __init__(self, l, L):
        self.l = l
        self.L = L

    def area(self):
        area = self.l * self.L
        return area

    def perimeter(self):
        per = 2 * (self.l + self.L)
        return per

    def __str__(self):
        return "Area of the rectangle is: " + str(self.area()) + " and the perimeter of the rectangle is: " + str(
            self.perimeter())


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def perimeter(self):
        per = self.a + self.b + self.c
        return per

    def __str__(self):
        return "Area of the triangle is: " + str(self.area()) + " and the perimeter of the triangle is: " + str(
            self.perimeter())


for shape in [Circle(3),Rectangle(3,6),Triangle(2,5,6)]:
    print(shape)