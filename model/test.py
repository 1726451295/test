import unittest

from generator import random_flag

class MyTestCase(unittest.TestCase):
    def test_something(self,flag):
        self.assertEqual(random_flag(self, flag))


if __name__ == '__main__':
    unittest.main()