import unittest
from elements.addi import Addi
from common import Value

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.addier = Addi()
        self.value_a = Value(5)
        self.value_b = Value(4)
        
    def test_connectInputs(self):
        self.addier.connectInputs([self.value_a, self.value_b])
        self.assertEqual(self.addier.value_a.value, 5)
        self.assertEqual(self.addier.value_b.value, 4)
        
    def test_writeOutput(self):
        self.addier.connectInputs([self.value_a, self.value_b])
        self.addier.writeOutput()
        self.assertEqual(self.addier.result.value, 9)
