import unittest
from elements.sub import Sub
from common import Value

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.Sub = Sub()
        self.value_a = Value(5)
        self.value_b = Value(4)
        
    def test_connectInputs(self):
        self.Sub.connectInputs([self.value_a, self.value_b])
        self.assertEqual(self.Sub.value_a.value, 5)
        self.assertEqual(self.Sub.value_b.value, 4)
        
    def test_writeOutput(self):
        self.Sub.connectInputs([self.value_a, self.value_b])
        self.Sub.writeOutput()
        self.assertEqual(self.Sub.result.value, 1)
