import unittest


class MyTestCase(unittest.TestCase):
    def test_kata_string(self):
        # Verify whether the Kata class __str__ works as expected
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
