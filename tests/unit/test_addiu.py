import unittest
from elements.addiu import Addiu
from common import Value

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.addiuer = Addiu()
        self.value_a = Value(5)
        self.value_b = Value(4)
        
    def test_connectInputs(self):
        self.addiuer.connectInputs([self.value_a, self.value_b])
        self.assertEqual(self.addiuer.value_a.value, 5)
        self.assertEqual(self.addiuer.value_b.value, 4)
        
    def test_writeOutput(self):
        self.addiuer.connectInputs([self.value_a, self.value_b])
        self.addiuer.writeOutput()
        self.assertEqual(self.addiuer.result.value, 9)
