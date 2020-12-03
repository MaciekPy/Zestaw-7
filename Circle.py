import unittest
import math
from Point import Point


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        print("Circle ( {1}, {2}, {3}" .format(
            self.pt.x, self.pt.y, self.radius))

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return math.pi * self.radius ** 2

    def move(self, x, y):     # przesuniecie o (x, y)
        self.pt.x = self.pt.x + x
        self.pt.y = self.pt.y + y
        return Circle(self.pt.x, self.pt.y, self.radius)

    def cover(self, other):   # najmniejszy okrąg pokrywający oba
        if self.radius > other.radius:
            cover_circle = self
        else:
            cover_circle = other

        cover_x = (self.pt.x + other.pt.x) // 2
        cover_y = (self.pt.y + other.pt.y) // 2

        cent_radius = math.sqrt(pow(cover_circle.pt.x - cover_x, 2) +
                                pow(cover_circle.pt.y - cover_y, 2))

        cover_circle.pt = Point(cover_x, cover_y)
        cover_circle.radius = cover_circle.radius + cent_radius
        return cover_circle
# Kod testujący moduł.


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle1 = Circle(1, 2, 3)
        self.circle2 = Circle(-1, -2, 3)

    def test_eq(self):
        self.assertEqual(self.circle1.__eq__(self.circle2), False)

    def test_area(self):
        self.assertEqual(self.circle1.area(), 9*math.pi)

    def test_move(self):
        self.assertEqual(self.circle1.move(5, 5), Circle(6, 7, 3))

    def test_cover(self):
        self.assertEqual(self.circle1.cover(self.circle2),
                         Circle(0, 0, (3 + math.sqrt(5))))


if __name__ == '__main__':
    unittest.main()
