import unittest
from elements.beq import Beq
from common import Value

class Testbeq(unittest.TestCase):
    def setUp(self):
        self.beq = Beq()
        self.value_a = Value(1)
        self.value_b = Value(2)

        self.jump_signal = Value(0)
        
    def test_connectInputs(self):
        self.beq.connectInputs([self.value_a, self.value_b])
        self.assertEqual(self.beq.value_a.value, 1)
        self.assertEqual(self.beq.value_b.value, 2)
        
    def test_writeOutput(self):
        self.beq.connectInputs([self.value_a, self.value_b])
        self.beq.writeOutput()
        self.assertEqual(self.beq.jump_signal.value, 0)
