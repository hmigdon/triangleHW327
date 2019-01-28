import unittest
import Triangle

class TestTriangle(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def test1(self): #equilateral test
        a=b=c=3
        expected = "Equilateral triangle"
        actual = Triangle.classify_triangle(a,b,c)
        self.assertEqual(expected, actual, "Test for equilateral fails.")

    def test2(self): #Iso test
        a=b=3
        c=5
        expected = "Isosceles triangle"
        actual = Triangle.classify_triangle(a,b,c)
        self.assertEqual(expected, actual, "Test for Isosceles fails.")

    def test3(self): #Scalene test
        a=3
        b=4
        c=5
        expected = "Scalene triangle"
        actual = Triangle.classify_triangle(a,b,c)
        self.assertEqual(expected, actual, "Test for Isosceles fails.")



if __name__ == '__main__':
    unittest.main(exit=False)

