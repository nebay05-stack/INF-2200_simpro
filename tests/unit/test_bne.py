import unittest
from elements.bne import Bne
from common import Value

class Testbne(unittest.TestCase): #if y and x are different, send signal, if same, don't send.
    def setUp(self):
        self.bne = Bne()
        self.value_a = Value(1)
        self.value_b = Value(2)

        self.jump_signal = Value(0)
        
    def test_connectInputs(self):
        self.bne.connectInputs([self.value_a, self.value_b])
        self.assertEqual(self.bne.value_a.value, 1)
        self.assertEqual(self.bne.value_b.value, 2)
        
    def test_writeOutput(self):
        self.bne.connectInputs([self.value_a, self.value_b])
        self.bne.writeOutput()
        self.assertEqual(self.bne.jump_signal.value, 1)
