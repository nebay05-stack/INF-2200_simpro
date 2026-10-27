import unittest
from elements.signextend import Signextend
from common import Value

class TestSignextend(unittest.TestCase):
    def setUp(self):
        self.signextend = Signextend()
        
    def test_connectInputs(self):
        input_value = Value(0x0005)
        self.signextend.connectInputs([input_value])
        self.assertEqual(input_value.value, 5)

    def write_output_positic(self):
        input_value = Value(0x0005)
        self.signextend.connectInputs([input_value])
        self.signextend.writeOutput()
        self.assertEqual(self.signextend.result.value, 5)

        
    def test_writeOutput(self):
        input_value = Value(0x8000)
        self.signextend.connectInputs([input_value])
        self.signextend.writeOutput()
        self.assertEqual(self.signextend.result.value, 0xFFFF8000)
