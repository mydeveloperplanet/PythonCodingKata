import unittest

from kata import Kata


class MyTestCase(unittest.TestCase):
    def test_kata_string(self):
        new_kata = Kata(1, 'This is a kata')
        self.assertEqual('\nFrom __str__\nnumber: 1, text: This is a kata', str(new_kata))


if __name__ == '__main__':
    unittest.main()
