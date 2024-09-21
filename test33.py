import unittest

def upper(str):
    return str.upper()

def lower(str):
    return str.lower()

def uppercheck(str):
    if str.isupper():
        return True

def lowercheck(str):
    if str.islower():
        return True

class TestStringMethods(unittest.TestCase):

    def test_1(self):

        result = upper('abc')

        self.assertEqual(result, 'ABC')

    def test_2(self):

        result = lower('abc')

        self.assertEqual(result, 'abc')

    


if __name__ == '__main__':
    unittest.main()
