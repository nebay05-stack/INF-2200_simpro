from common import Value
from elements.cpuElement import CPUElement
from typing import List

class JumpSlicer(CPUElement):
    def __init__(self):
        # Inputy
        self.pc_plus_4: Value = Value(0)
        self.shifted_jump_adress: Value = Value(0)
        
        # Output
        self.full_jump_adress = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'jump_slicer should have two inputs'
        
        # Inputs
        self.pc_plus_4 = inputs[0]
        self.shifted_jump_adress = inputs[0]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.pc_plus_4.value, int) and isinstance(self.shifted_jump_adress.value, int)

        highestpc_4 = top_4_pc = self.pc_plus_4 & 0xF0000000
        self.full_jump_adress = highestpc_4 | self.shifted_jump_adress