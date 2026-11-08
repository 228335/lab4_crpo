import unittest
import math
from geometric_lib import circle, rectangle, square, triangle

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        # Тест площади круга с радиусом 5
        res = circle.area(5)
        self.assertAlmostEqual(res, math.pi * 25)

    def test_perimeter(self):
        # Тест периметра круга с радиусом 5
        res = circle.perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)

    def test_zero_area(self):
        # Тест площади при нулевом радиусе
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_below_0(self):
        # Тест площади при нулевом радиусе
        res = circle.area(-5)
        self.assertEqual(res, 10 * math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        # Тест площади прямоугольника 10 на 5
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_perimeter(self):
        # Тест периметра прямоугольника 10 на 5
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_zero_mul(self):
        # Тест площади при одной из сторон равной 0
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_below_0(self):
        # Тест площади при нулевом радиусе
        res = rectangle.area(10, -5)
        self.assertEqual(res, 30)



class SquareTestCase(unittest.TestCase):
    def test_area(self):
        # Тест площади квадрата со стороной 5
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        # Тест периметра квадрата со стороной 5
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_below_0(self):
        # Тест периметра квадрата со стороной 5
        res = square.perimeter(-5)
        self.assertEqual(res, 20)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        # Тест площади треугольника (основание 10, высота 5)
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        # Тест периметра треугольника со сторонами 3, 4, 5
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_area(self):
        # Тест площади при высоте равной 0
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_below_0(self):
        # Тест периметра квадрата со стороной 5
        res = triangle.perimeter(-3, 4, 5)
        self.assertEqual(res, 12)

if __name__ == '__main__':
    unittest.main()