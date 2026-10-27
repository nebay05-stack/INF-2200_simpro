import unittest
from elements.memory import Memory
from common import Value

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memfile = "src/memfiles/selectionsort.mem"
        self.memory = Memory(self.memfile)

        
    def test_connectInputs(self):
        self.assertTrue(len(self.memory.memory) > 0)
        self.assertIn(0xbfc00000, self.memory.memory)
        self.assertEqual(self.memory.memory[0xbfc00000], 0x3c10c000)
       

    def test_writeOutput(self):
        try:
            self.memory.printAll()
        except Exception as e:
            self.memfile(f"printAll() feilet med unntak: {e}")