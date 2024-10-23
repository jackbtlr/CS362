import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertIsNone(contrived_func(21))
    pass

    def test2(self):
        self.assertIsNone(contrived_func(-3))
    pass

    def test3(self):
        self.assertIsNone(contrived_func(3))
    pass

    def test4(self):
        self.assertIsNone(contrived_func(12))
    pass

    def test5(self):
        self.assertIsNone(contrived_func(24))
    pass

    def test6(self):
        self.assertIsNone(contrived_func(-8))
    pass

    def test7(self):
        self.assertIsNone(contrived_func(18))
    pass

    def test8(self):
        self.assertIsNone(contrived_func(19))
    pass


if __name__ == '__main__':
    unittest.main()
