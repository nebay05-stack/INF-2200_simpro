import unittest
from elements.addu import Addu
from common import Value

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.adduer = Addu()
        self.value_a = Value(5)
        self.value_b = Value(4)
        
    def test_connectInputs(self):
        self.adduer.connectInputs([self.value_a, self.value_b])
        self.assertEqual(self.adduer.value_a.value, 5)
        self.assertEqual(self.adduer.value_b.value, 4)
        
    def test_writeOutput(self):
        self.adduer.connectInputs([self.value_a, self.value_b])
        self.adduer.writeOutput()
        self.assertEqual(self.adduer.result.value, 9)
