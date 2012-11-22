import unittest


class TestCase(unittest.TestCase):

    def test_one(self):
        one = 1
        self.assertEqual(one, 1)

    def test_two(self):
        two = 2
        self.assertEqual(two, 2)
