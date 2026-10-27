import unittest
from elements.mux import Mux
from common import Value

class TestMux(unittest.TestCase):
    def setUp(self):
        self.mux = Mux()
        self.input_zero = Value(5)
        self.input_one = Value(67)
        self.controll_signal = Value(0)

    
        
    def test_connectInputs(self):
        self.mux.connectInputs([self.input_zero, self.input_one, self.controll_signal])
        self.assertEqual(self.mux.inputZero.value, 5)
        self.assertEqual(self.mux.inputOne.value, 67)
        self.assertEqual(self.mux.controlSignal.value, 0)
        
    def test_writeOutput_zero(self):
        self.mux.connectInputs([self.input_zero, self.input_one, self.controll_signal])
        self.mux.writeOutput()
        self.assertEqual(self.mux.output.value, 5)

    def test_writeOutput_one(self):
        self.controll_signal.value = 1
        self.mux.connectInputs([self.input_zero, self.input_one, self.controll_signal])
        self.mux.writeOutput()
        self.assertEqual(self.mux.output.value, 67)
