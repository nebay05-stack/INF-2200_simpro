import unittest
from elements.jump_slicer import JumpSlicer
from common import Value

class TestJumpSlicer(unittest.TestCase):
    def setUp(self):
        self.jump_slicer = JumpSlicer()

        self.pc_plus_4 = Value(0xbfc00004)
        self.shift_jump_addrss = Value(0x0fc000f0)
        
    def test_connectInputs(self):
        self.jump_slicer.connectInputs([self.pc_plus_4, self.shift_jump_addrss])
        self.assertEqual(self.jump_slicer.pc_plus_4.value, 0xbfc00004)
        self.assertEqual(self.jump_slicer.shifted_jump_adress.value, 0x0fc000f0)

    def test_writeOutput(self):
        self.jump_slicer.connectInputs([self.pc_plus_4, self.shift_jump_addrss])
        self.jump_slicer.writeOutput()
        expected_address = 0xbfc000f0
        self.assertEqual(self.jump_slicer.full_jump_adress.value, expected_address)

        
