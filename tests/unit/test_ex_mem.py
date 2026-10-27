import unittest
from elements.EX_MEM import Ex_mem
from common import Value

class TestEx_mem(unittest.TestCase):
    def setUp(self):
        self.ex_mem = Ex_mem()
        self.alu_result = Value(0x1004)
        self.read_data2 = Value(67)
        self.reg_dst = Value(10)

        self.MemtoReg = Value(0)
        self.MemRead = Value(1)
        self.MemWrite = Value(0)
        self.RegWrite = Value(1)
        self.Break = Value(0)
        
        


    def test_connectInputs(self):
        self.ex_mem.connectInputs([self.alu_result, self.read_data2, self.reg_dst, self.MemtoReg, self.MemRead, self.MemWrite, self.RegWrite, self.Break])
        self.assertEqual(self.ex_mem.alu_result_inp.value, 0x1004)
        self.assertEqual(self.ex_mem.readdata_2_inp.value, 67)
        self.assertEqual(self.ex_mem.reg_dst_inp.value, 10)
        self.assertEqual(self.ex_mem.controll_signal_inp['MemtoReg'].value, 0)
        self.assertEqual(self.ex_mem.controll_signal_inp['MemRead'].value, 1)
        self.assertEqual(self.ex_mem.controll_signal_inp['MemWrite'].value, 0)
        self.assertEqual(self.ex_mem.controll_signal_inp['RegWrite'].value, 1)
        self.assertEqual(self.ex_mem.controll_signal_inp['Break'].value, 0)
        
    def test_writeOutput(self):
        self.ex_mem.connectInputs([self.alu_result, self.read_data2, self.reg_dst, self.MemtoReg, self.MemRead, self.MemWrite, self.RegWrite, self.Break])
        self.ex_mem.writeOutput()
        self.assertEqual(self.ex_mem.alu_result_out.value, 0x1004)
        self.assertEqual(self.ex_mem.readdata_2_out.value, 67)
        self.assertEqual(self.ex_mem.reg_dst_out.value, 10)
        self.assertEqual(self.ex_mem.controll_signal_out['MemtoReg'].value, 0)
        self.assertEqual(self.ex_mem.controll_signal_out['MemRead'].value, 1)
        self.assertEqual(self.ex_mem.controll_signal_out['MemWrite'].value, 0)
        self.assertEqual(self.ex_mem.controll_signal_out['RegWrite'].value, 1)
        self.assertEqual(self.ex_mem.controll_signal_out['Break'].value, 0)

    