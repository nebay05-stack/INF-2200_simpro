import unittest
from elements.controll_unit import Controller
from common import Value

class Test_Controller(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.oppcode = Value(0)
        
    def test_connectInputs(self):
        self.controller.connectInputs([self.oppcode])
        self.assertEqual(self.controller.oppcode.value, 0)
        
    def test_writeOutput(self):
        self.controller.connectInputs([self.oppcode])
        self.controller.writeOutput()
        self.assertEqual(self.RegDst.value, 0)
        self.assertEqual(self.ALUSrc.value, 0)
        self.assertEqual(self.RegWrite.value, 0)
        self.assertEqual(self.ALUOp.value, 0)
