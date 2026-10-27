import unittest
from elements.dataMemory import DataMemory
from common import Value

class TestDatamemory(unittest.TestCase):
    def setUp(self):
        self.memfile = "src/memfiles/selectionsort.mem"
        self.datamemory = DataMemory(self.memfile)

        self.valid_addres = Value(0xc0000000)
        self.writedata = Value(57)
        self.MemRead = Value(1)
        self.MemWrite = Value(0)
        
    def test_connectInputs(self):
        self.datamemory.connectInputs([self.valid_addres, self.writedata, self.MemRead, self.MemWrite])
        self.assertEqual(self.datamemory.address.value, 0xc0000000)
        self.assertEqual(self.datamemory.writedata.value, 57)

    def test_writeOutput_read(self):
        self.datamemory.connectInputs([self.valid_addres, self.writedata, self.MemRead, self.MemWrite])
        self.datamemory.writeOutput()
        self.assertEqual(self.datamemory.readdata.value, 0xd)

        
    def test_writeOutput_write(self):
        new_address = Value(0xc0000100)
        self.writedata.value = 99
        self.MemRead.value = 0
        self.MemWrite.value = 1
        self.datamemory.connectInputs([new_address, self.writedata, self.MemRead, self.MemWrite])
        self.datamemory.writeOutput()
        self.assertEqual(self.datamemory.memory[0xc0000100], 99)
