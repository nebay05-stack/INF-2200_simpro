import unittest
from elements.ID_EX import Id_ex
from common import Value

class TestId_ex(unittest.TestCase):
    def setUp(self):
        self.id_ex = Id_ex()
        self.readdata_1 = Value(34)
        self.readdata_2 = Value(67)
        self.signextend = Value(4)
        self.rt = Value(9)
        self.rd = Value(10)

        self.flush_signal = Value(0)
        self.function = Value(32)

        self.RegDst = Value(1)
        self.MemRead = Value(0)
        self.MemtoReg = Value(0)
        self.ALUOp = Value(2)
        self.MemWrite = Value(0)
        self.ALUSrc = Value(0)
        self.RegWrite = Value(1)



    def test_connectInputs(self):
        self.id_ex.connectInputs([self.readdata_1, self.readdata_2, self.signextend, self.rt, self.rd, self.flush_signal, self.function, self.RegDst, self.MemRead, self.MemtoReg, self.ALUOp, self.MemWrite, self.ALUSrc, self.RegWrite])
        self.assertEqual(self.id_ex.readdata_1_inp.value, 34)
        self.assertEqual(self.id_ex.readdata_2_inp.value, 67)
        self.assertEqual(self.id_ex.signextend_inp.value, 4)
        self.assertEqual(self.id_ex.rt_inp.value, 9)
        self.assertEqual(self.id_ex.rd_inp.value, 10)
        self.assertEqual(self.id_ex.function_inp.value, 32)
        self.assertEqual(self.id_ex.controll_signal_inp['RegDst'].value, 1)
        self.assertEqual(self.id_ex.controll_signal_inp['MemRead'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_inp['MemtoReg'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_inp['ALUOp'].value, 2)
        self.assertEqual(self.id_ex.controll_signal_inp['MemWrite'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_inp['ALUSrc'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_inp['RegWrite'].value, 1)
        self.assertEqual(self.id_ex.controll_signal_inp['Break'].value, 0)
        
    def test_writeOutput_normal(self):
        self.id_ex.connectInputs([self.readdata_1, self.readdata_2, self.signextend, self.rt, self.rd, self.flush_signal, self.function, self.RegDst, self.MemRead, self.MemtoReg, self.ALUOp, self.MemWrite, self.ALUSrc, self.RegWrite])
        self.id_ex.writeOutput()
        self.assertEqual(self.id_ex.readdata_1_out.value, 34)
        self.assertEqual(self.id_ex.readdata_2_out.value, 67)
        self.assertEqual(self.id_ex.signextend_out.value, 4)
        self.assertEqual(self.id_ex.rt_out.value, 9)
        self.assertEqual(self.id_ex.rd_out.value, 10)
        self.assertEqual(self.id_ex.function_out.value, 32)
        self.assertEqual(self.id_ex.controll_signal_out['RegDst'].value, 1)
        self.assertEqual(self.id_ex.controll_signal_out['MemRead'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['MemtoReg'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['ALUOp'].value, 2)
        self.assertEqual(self.id_ex.controll_signal_out['MemWrite'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['ALUSrc'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['RegWrite'].value, 1)
        self.assertEqual(self.id_ex.controll_signal_out['Break'].value, 0)


    def test_writeOutput_flushed(self):
        self.flush_signal.value = 1
        self.id_ex.connectInputs([self.readdata_1, self.readdata_2, self.signextend, self.rt, self.rd, self.flush_signal, self.function, self.RegDst, self.MemRead, self.MemtoReg, self.ALUOp, self.MemWrite, self.ALUSrc, self.RegWrite])
        self.id_ex.writeOutput()
        self.assertEqual(self.id_ex.readdata_1_out.value, 0)
        self.assertEqual(self.id_ex.readdata_2_out.value, 0)
        self.assertEqual(self.id_ex.signextend_out.value, 0)
        self.assertEqual(self.id_ex.rt_out.value, 0)
        self.assertEqual(self.id_ex.rd_out.value, 0)
        self.assertEqual(self.id_ex.function_out.value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['RegDst'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['MemRead'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['MemtoReg'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['ALUOp'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['MemWrite'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['ALUSrc'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['RegWrite'].value, 0)
        self.assertEqual(self.id_ex.controll_signal_out['Break'].value, 0)

    