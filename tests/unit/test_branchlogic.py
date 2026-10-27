import unittest
from elements.branch_logic import Branch_logic
from common import Value

class TestBranchLogic(unittest.TestCase):
    def setUp(self):
        self.branch_logic = Branch_logic()
        self.branch = Value(0)
        self.bne_bit = Value(0)
        self.readdata_1 = Value(10)
        self.readdata_2 = Value(10)

        
    def test_connectInputs(self):
        self.branch_logic.connectInputs([self.branch, self.bne_bit, self.readdata_1, self.readdata_2])
        self.assertEqual(self.branch_logic.readdata_1.value, 10)
        self.assertEqual(self.branch_logic.readdata_2.value, 10)

    def test_writeOutput_beq_taken(self):
        self.branch.value = 1
        self.branch_logic.connectInputs([self.branch, self.bne_bit, self.readdata_1, self.readdata_2])
        self.branch_logic.writeOutput()
        self.assertEqual(self.branch_logic.branch_taken.value, 1)

        
    def test_writeOutput_beq_not_taken(self):
        self.branch.value = 1
        self.readdata_2.value = 20
        self.branch_logic.connectInputs([self.branch, self.bne_bit, self.readdata_1, self.readdata_2])
        self.branch_logic.writeOutput()
        self.assertEqual(self.branch_logic.branch_taken.value, 0)

    def test_writeOutput_bne_taken(self):
        self.branch.value = 1
        self.bne_bit.value = 1
        self.readdata_2.value = 20
        self.branch_logic.connectInputs([self.branch, self.bne_bit, self.readdata_1, self.readdata_2])
        self.branch_logic.writeOutput()
        self.assertEqual(self.branch_logic.branch_taken.value, 1)

    def test_writeOutput_bne_taken(self):
        self.branch.value = 1
        self.bne_bit.value = 1
        self.readdata_2.value = 10
        self.branch_logic.connectInputs([self.branch, self.bne_bit, self.readdata_1, self.readdata_2])
        self.branch_logic.writeOutput()
        self.assertEqual(self.branch_logic.branch_taken.value, 0)


    def test_writeOutput_no_branch(self):
        self.branch.value = 0
        self.bne_bit.value = 0
        self.readdata_2.value = 20
        self.branch_logic.connectInputs([self.branch, self.bne_bit, self.readdata_1, self.readdata_2])
        self.branch_logic.writeOutput()
        self.assertEqual(self.branch_logic.branch_taken.value, 0)
