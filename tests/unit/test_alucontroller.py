import unittest
from elements.alu_kontroller import AluController
from common import Value

class TestAluController(unittest.TestCase):
    def setUp(self):
        self.alu_controller = AluController()
        self.ALUOp = Value(0)
        self.Function = Value(0)
        
    def test_connectInputs(self):
        self.alu_controller.connectInputs([self.ALUOp, self.Function])
        self.assertEqual(self.alu_controller.alu_op.value, 0)
        self.assertEqual(self.alu_controller.function.value, 0)
        
    def test_writeOutput_lw_sw_addi(self):
        self.ALUOp.value = 0b00
        self.alu_controller.connectInputs([self.ALUOp, self.Function])
        self.alu_controller.writeOutput()
        self.assertEqual(self.alu_controller.alu_control_out.value, 0b0010)

    def test_writeOutput_branch(self):
        self.ALUOp.value = 0b01
        self.alu_controller.connectInputs([self.ALUOp, self.Function])
        self.alu_controller.writeOutput()
        self.assertEqual(self.alu_controller.alu_control_out.value, 0b0110)

    def test_writeOutput_lui(self):
        self.ALUOp.value = 0b11
        self.alu_controller.connectInputs([self.ALUOp, self.Function])
        self.alu_controller.writeOutput()
        self.assertEqual(self.alu_controller.alu_control_out.value, 0b1111)

    def test_writeOutput_rtype_add(self):
        self.ALUOp.value = 0b10
        self.Function.value = 0b100000
        self.alu_controller.connectInputs([self.ALUOp, self.Function])
        self.alu_controller.writeOutput()
        self.assertEqual(self.alu_controller.alu_control_out.value, 0b0010)

    def test_writeOutput_rtype_add(self):
        self.ALUOp.value = 0b10
        self.Function.value = 0b101010
        self.alu_controller.connectInputs([self.ALUOp, self.Function])
        self.alu_controller.writeOutput()
        self.assertEqual(self.alu_controller.alu_control_out.value, 0b0111)

