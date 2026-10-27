import unittest
from elements.registerFile import RegisterFile
from common import Value

class Testregisterfil(unittest.TestCase): 
    def setUp(self):
        self.registerfil = RegisterFile()
        self.read_1 = Value(9)
        self.read_2 = Value(10)
        self.writereg = Value(9)
        self.writedata = Value(67)
        self.RegWrite = Value(1)
        
    def test_connectInputs(self):
        self.registerfil.connectInputs([self.read_1, self.read_2, self.writereg, self.writedata, self.RegWrite])
        self.assertEqual(self.registerfil.readregister_1.value, 9)
        self.assertEqual(self.registerfil.readregister_2.value, 10)
        
    def test_writeOutput_normal(self):
        self.registerfil.connectInputs([self.read_1, self.read_2, self.writereg, self.writedata, self.RegWrite])
        self.registerfil.writeOutput()
        self.assertEqual(self.registerfil.register[9], 67)

    def test_writeOutput_zero(self):
        writereg_zero = Value(0)
        self.registerfil.connectInputs([self.read_1, self.read_2, writereg_zero, self.writedata, self.RegWrite])
        self.registerfil.writeOutput()
        self.assertEqual(self.registerfil.register[0], 0)

    def test_writeOutput_disabled(self):
        RegWrite = Value(0)
        self.registerfil.connectInputs([self.read_1, self.read_2, self.writereg, self.writedata, RegWrite])
        self.registerfil.writeOutput()
        self.assertEqual(self.registerfil.register[9], 0)

    def test_read_register(self):
        self.registerfil.register[9] = 100
        self.registerfil.register[10] = 67

        self.registerfil.connectInputs([self.read_1, self.read_2, self.writereg, self.writedata, self.RegWrite])
        self.registerfil.read_register()
        self.assertEqual(self.registerfil.readdata_1.value, 100)
        self.assertEqual(self.registerfil.readdata_2.value, 67)

    
