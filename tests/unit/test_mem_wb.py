import unittest
from elements.MEN_WB import Mem_wb
from common import Value

class TestMem_web(unittest.TestCase):
    def setUp(self):
        self.mem_wb = Mem_wb()
        self.read_data = Value(67)
        self.alu_result = Value(0x1004)
        self.reg_dst = Value(10)

        self.MemtoReg = Value(1)
        self.RegWrite = Value(1)
        self.Break = Value(0)
        
        


    def test_connectInputs(self):
        self.mem_wb.connectInputs([self.read_data, self.alu_result, self.reg_dst, self.MemtoReg, self.RegWrite, self.Break])
        self.assertEqual(self.mem_wb.read_data_inp.value, 67)
        self.assertEqual(self.mem_wb.alu_result_inp.value, 0x1004)
        self.assertEqual(self.mem_wb.reg_dst_inp.value, 10)
        self.assertEqual(self.mem_wb.controll_signal_inp['MemtoReg'].value, 1)
        self.assertEqual(self.mem_wb.controll_signal_inp['RegWrite'].value, 1)
        self.assertEqual(self.mem_wb.controll_signal_inp['Break'].value, 0)
        
    def test_writeOutput(self):
        self.mem_wb.connectInputs([self.read_data, self.alu_result, self.reg_dst, self.MemtoReg, self.RegWrite, self.Break])
        self.mem_wb.writeOutput()
        self.assertEqual(self.mem_wb.read_data_out.value, 67)
        self.assertEqual(self.mem_wb.alu_result_out.value, 0x1004)
        self.assertEqual(self.mem_wb.reg_dst_out.value, 10)
        self.assertEqual(self.mem_wb.controll_signal_out['MemtoReg'].value, 1)
        self.assertEqual(self.mem_wb.controll_signal_out['RegWrite'].value, 1)
        self.assertEqual(self.mem_wb.controll_signal_out['Break'].value, 0)

    