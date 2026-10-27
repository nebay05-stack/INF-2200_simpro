import unittest
from elements.constant import Constant
from common import Value

class TestConstant(unittest.TestCase):
    def setUp(self):
        self.constant_4 = Constant(4)

        
    def test_connectInputs(self):
        self.constant_4.connectInputs([])
        self.assertEqual(self.constant_4.constantValue.value, 4)
       

    def test_writeOutput(self):
        self.constant_4.connectInputs([])
        self.constant_4.writeOutput()
        self.assertEqual(self.constant_4.constantValue.value, 4)

        