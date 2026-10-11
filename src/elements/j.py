from common import Value
from elements.cpuElement import CPUElement
from typing import List

class J(CPUElement):
    def __init__(self):
        # Inputs
        self.pc_4: Value = Value(0)
        self.instruction_adress: Value = Value(0)

        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'j should have two inputs'
          
        # Inputs
        self.pc_4 = inputs[0]
        self.instruction_adress = input[1]
        
    def writeOutput(self):
        assert isinstance(self.pc_4, int) and isinstance(self.instruction_adress, int) 
        pc_adress = self.pc_4.value & 0xf0000000
        shift_op = (self.instruction_adress.value << 2) & 0xffffffff

        self.result.value = pc_adress + shift_op
        