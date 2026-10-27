import unittest
from elements.shiftle import Shiftleft
from common import Value

class TestShiftleft(unittest.TestCase):
    def setUp(self):
        self.Shiftleft = Shiftleft()
        self.input_value = Value(2)
        self.Shiftleft.connectInputs
        
    def test_connectInputs(self):
        self.Shiftleft.connectInputs([self.input_value])
        self.assertEqual(self.Shiftleft.value_a.value, 2)
     
        
    def test_writeOutput(self):
        self.Shiftleft.connectInputs([self.input_value])
        self.Shiftleft.writeOutput()
        self.assertEqual(self.Shiftleft.result.value, 8)
