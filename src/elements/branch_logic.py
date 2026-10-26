from typing import List
from common import Value
from .cpuElement import CPUElement


class Branch_logic(CPUElement):
    def __init__(self):
        # Inputs
        self.branch: Value = Value(0)
        self.bne_bit: Value = Value(0)
        self.readdata_1: Value = Value(0)
        self.readdata_2: Value = Value(0)
        # Output
        self.branch_taken: Value = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 4, "branch_logic should have 4 inputs"
        self.branch = inputs[0]
        self.bne_bit = inputs[1]
        self.readdata_1 = inputs[2]
        self.readdata_2 = inputs[3]

    def writeOutput(self):
        assert isinstance(self.branch.value, int) and isinstance(self.bne_bit.value, int) and isinstance(self.readdata_1.value, int) and isinstance(self.readdata_2.value, int)

        equal = self.readdata_1.value == self.readdata_2.value

        if self.branch.value == 1 and self.bne_bit.value == 0:
            taken = equal 
        elif self.branch.value == 1 and self.bne_bit.value == 1:
            taken = not equal 
        else:
            taken = False   

        if taken:
            self.branch_taken.value = 1
        else: 
            self.branch_taken.value = 0