import unittest
from elements.alu import Alu
from common import Value

class TestAlu(unittest.TestCase):
    def setUp(self):
        self.alu = Alu()
        self.val_1 = Value(10)
        self.val_2 = Value(20)
        self.alu_controller = Value(0b0010)

        
    def test_connectInputs(self):
        self.alu.connectInputs([self.val_1, self.val_2, self.alu_controller])
        self.assertEqual(self.alu.source_1.value, 10)
        self.assertEqual(self.alu.source_2.value, 20)
        self.assertEqual(self.alu.alu_control.value, 0b0010)

    def test_writeOutput_add(self):
        self.alu.connectInputs([self.val_1, self.val_2, self.alu_controller])
        self.alu.writeOutput()
        self.assertEqual(self.alu.result.value, 30)
        self.assertEqual(self.alu.zero.value, 0)
        self.assertEqual(self.alu.overflow.value, 0)

        
    def test_writeOutput_sub_and_zero(self):
        self.val_1.value = 20
        self.val_2.value = 20
        self.alu_controller.value = 0b0110
        self.alu.connectInputs([self.val_1, self.val_2, self.alu_controller])
        self.alu.writeOutput()
        self.assertEqual(self.alu.result.value, 0)
        self.assertEqual(self.alu.zero.value, 1)

    def test_writeOutput_slt(self):
        self.alu_controller.value = 0b0111
        self.alu.connectInputs([self.val_1, self.val_2, self.alu_controller])
        self.alu.writeOutput()
        self.assertEqual(self.alu.result.value, 1)

    def test_writeOutput_overflow(self):
            self.val_1.value = 0x7FFFFFFF
            self.val_2.value = 1
            self.alu_controller.value = 0b0010
            self.alu.connectInputs([self.val_1, self.val_2, self.alu_controller])
            self.alu.writeOutput()
            self.assertEqual(self.alu.overflow.value, 1)
        



    


    
