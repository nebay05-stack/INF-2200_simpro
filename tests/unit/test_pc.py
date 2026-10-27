import unittest
from elements.pc import PC
from common import Value

class TestPc(unittest.TestCase):
    def setUp(self):
        self.base_addr = 0
        self.pc = PC(self.base_addr)
        self.next_addr = Value(4)
        self.pc_write = Value(1)
        
    def test_connectInputs(self):
        self.pc.connectInputs([self.next_addr, self.pc_write])
        self.assertEqual(self.pc.incomingAddress.value, self.base_addr)
        self.assertEqual(self.pc.pc_write.value, 1)
        
    def test_writeOutput(self):
        self.pc.connectInputs([self.next_addr, self.pc_write])
        self.next_addr.value = 4
        self.pc.writeOutput()
        self.assertEqual(self.pc.currentAddress.value, 4)

    def test_writeOutput_stalled(self):
        pc_write = Value(0)
        self.pc.currentAddress.value = 8
        self.pc.connectInputs([self.next_addr, pc_write])
        self.next_addr.value = 12
        self.pc.writeOutput()
        self.assertEqual(self.pc.currentAddress.value, 8)
