import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = add(10,5)
        self.assertEquals(result,15)