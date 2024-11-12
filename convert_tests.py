import unittest
import convert

class TestCases(unittest.TestCase):

    #Test 1
    def testStrToFloat1(self):
        input = "98.325"
        expected = 98.325
        result = convert.str_to_float(input)
        self.assertEqual(expected, result)

    #Test 2
    def testStrToFloat2(self):
        input = "room"
        expected = None
        result = convert.str_to_float(input)
        self.assertEqual(expected, result)

    #Test 3
    def testStrToFloat3(self):
        input = "25"
        expected = None
        result = convert.str_to_float(input)
        self.assertEqual(expected, result)


    if __name__ == '__main__':
        unittest.main()
