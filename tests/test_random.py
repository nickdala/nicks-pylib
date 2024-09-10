import unittest

from nickspylib.random import generate_random_number

class MyTestCase(unittest.TestCase):
    def test_something(self):
        num = generate_random_number(3, 10)
        self.assertTrue(num >= 3)
        self.assertTrue(num < 10)

if __name__ == '__main__':
    unittest.main()