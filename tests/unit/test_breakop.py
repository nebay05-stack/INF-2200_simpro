import unittest
from elements.break_op import Break_op
from common import Value

class TestBreakop(unittest.TestCase):
    def setUp(self):
        self.breakop = Break_op()
        self.opcode = Value(0)
        self.break_function = Value(13)
        self.add_function = Value(32)

        self.full_stop = Value(0)
        
    def test_connectInputs(self):
        self.breakop.connectInputs([self.opcode, self.break_function])
        self.assertEqual(self.breakop.oppcode.value, 0)
        self.assertEqual(self.breakop.funtion.value, 13)

    def test_writeOutput_break_detection(self):
        self.breakop.connectInputs([self.opcode, self.break_function])
        self.breakop.writeOutput()
        self.assertEqual(self.breakop.full_stop.value, 1)

        
    def test_writeOutput_not_break(self):
        self.breakop.connectInputs([self.opcode, self.add_function])
        self.breakop.writeOutput()
        self.assertEqual(self.breakop.full_stop.value, 0)
