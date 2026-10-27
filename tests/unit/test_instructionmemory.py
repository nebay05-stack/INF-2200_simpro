import unittest
from elements.instructionMemory import InstructionMemory
from common import Value

class TestInstructionmemory(unittest.TestCase):
    def setUp(self):
        self.memfile = "src/memfiles/selectionsort.mem"
        self.instructionmemory = InstructionMemory(self.memfile)

        self.read_addres = Value(0xbfc00104)
        
    def test_connectInputs(self):
        self.instructionmemory.connectInputs([self.read_addres])
        self.assertEqual(self.instructionmemory.Readaddres.value, 0xbfc00104)

    def test_writeOutput_decode(self):
        self.instructionmemory.connectInputs([self.read_addres])
        self.instructionmemory.writeOutput()
        self.assertEqual(self.instructionmemory.oppcode.value, 0)
        self.assertEqual(self.instructionmemory.rs.value, 11)
        self.assertEqual(self.instructionmemory.rt.value, 0)
        self.assertEqual(self.instructionmemory.rd.value, 10)
        self.assertEqual(self.instructionmemory.function.value, 32)
        self.assertEqual(self.instructionmemory.imidiat.value, 0x5020)

        
