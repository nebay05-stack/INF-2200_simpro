import unittest
from elements.andop import Andop
from common import Value

class TestAnd(unittest.TestCase):
    def setUp(self):
        self.ander = Andop()
        self.value_a = Value(1)
        self.value_b = Value(0)
        
    def test_connectInputs(self):
        self.ander.connectInputs([self.value_a, self.value_b])
        self.assertEqual(self.ander.value_a.value, 1)
        self.assertEqual(self.ander.value_b.value, 0)
        
    def test_writeOutput(self):
        self.ander.connectInputs([self.value_a, self.value_b])
        self.ander.writeOutput()
        self.assertEqual(self.ander.result.value, False)
