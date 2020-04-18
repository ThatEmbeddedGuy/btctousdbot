import unittest
import rates

class TestStringMethods(unittest.TestCase):

    def test_empty_symbol(self):
        self.assertIsNone(rates.make_request(""))



if __name__ == '__main__':
    unittest.main()