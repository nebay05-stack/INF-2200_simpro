import unittest
from elements.controll_unit import Controller
from common import Value

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.oppcode = Value(0)
        
    def test_connectInputs(self):
        self.controller.connectInputs([self.oppcode])
        self.assertEqual(self.controller.oppcode.value, 0)
        
    def test_writeOutput(self):
        self.controller.connectInputs([self.oppcode])
        self.controller.writeOutput()
        self.assertEqual(self.controller.RegDst.value, 1)
        self.assertEqual(self.controller.ALUSrc.value, 0)
        self.assertEqual(self.controller.RegWrite.value, 1)
        self.assertEqual(self.controller.ALUOp.value, 0b10)
        self.assertEqual(self.controller.Branch.value, 0)
        self.assertEqual(self.controller.MemRead.value, 0)
        self.assertEqual(self.controller.MemtoReg.value, 0)
        self.assertEqual(self.controller.MemWrite.value, 0)
        self.assertEqual(self.controller.Jump.value, 0)
        self.assertEqual(self.controller.Bne_Bit.value, 0)
