import unittest
from elements.break_op import Break_op
from common import Value

class Testbreakop(unittest.TestCase):
    def setUp(self):
        self.breakop = Break_op()
        self.break_signal = Value(1)

        self.full_stop = Value(0)
        
    def test_connectInputs(self):
        self.breakop.connectInputs([self.break_signal])
        self.assertEqual(self.breakop.break_signal.value, 1)
        
    def test_writeOutput(self):
        self.breakop.connectInputs([self.break_signal])
        self.breakop.writeOutput()
        self.assertEqual(self.breakop.break_signal.value, 1)
