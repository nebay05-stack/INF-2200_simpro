import unittest
from elements.IF_ID import If_id
from common import Value

class TestIf_id(unittest.TestCase):
    def setUp(self):
        self.if_id = If_id()
        self.pc_plus_4 = Value(4)
        self.oppcode = Value(0)
        self.rs = Value(8)
        self.rt = Value(9)
        self.rd = Value(10)
        self.immidiat = Value(0x0005)
        self.function = Value(32)
        self.jump_addres = Value(0x0010)

        self.if_id_write = Value(1)
        self.flush_signal = Value(0)

    def test_connectInputs(self):
        self.if_id.connectInputs([self.pc_plus_4, self.oppcode, self.rs, self.rt, self.rd, self.immidiat, self.function, self.jump_addres, self.if_id_write, self.flush_signal])
        self.assertEqual(self.if_id.pc_plus_4_inp.value, 4)
        self.assertEqual(self.if_id_write.value, 1)
        
    def test_writeOutput_normal(self):
        self.if_id.connectInputs([self.pc_plus_4, self.oppcode, self.rs, self.rt, self.rd, self.immidiat, self.function, self.jump_addres, self.if_id_write, self.flush_signal])
        self.if_id.writeOutput()
        self.assertEqual(self.if_id.pc_plus_4_out.value, 4)
        self.assertEqual(self.if_id.rs_out.value, 8)
        self.assertEqual(self.if_id.rt_out.value, 9)
        self.assertEqual(self.if_id.rd_out.value, 10)
        self.assertEqual(self.if_id.function_out.value, 32)

    def test_writeOutput_stalled(self):
        self.if_id.connectInputs([self.pc_plus_4, self.oppcode, self.rs, self.rt, self.rd, self.immidiat, self.function, self.jump_addres, self.if_id_write, self.flush_signal])
        self.if_id.writeOutput()
        self.if_id_write.value = 0
        self.pc_plus_4.value = 8
        self.rs.value = 16
        self.if_id.writeOutput()
        self.assertEqual(self.if_id.pc_plus_4_out.value, 4)
        self.assertEqual(self.if_id.rs_out.value, 8)

    def test_writeOutput_flushed(self):
        self.flush_signal.value = 1
        self.if_id.connectInputs([self.pc_plus_4, self.oppcode, self.rs, self.rt, self.rd, self.immidiat, self.function, self.jump_addres, self.if_id_write, self.flush_signal])
        self.if_id.writeOutput()
        self.assertEqual(self.if_id.pc_plus_4_out.value, 0)
        self.assertEqual(self.if_id.rs_out.value, 0)
        self.assertEqual(self.if_id.rt_out.value, 0)
        self.assertEqual(self.if_id.rd_out.value, 0)
        self.assertEqual(self.if_id.function_out.value, 0)

    

