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
        assert len(inputs) == 2, 'jump_slicer should have 2 inputs'
        
        # Inputs
        self.pc_plus_4 = inputs[0]
        self.shifted_jump_adress = inputs[1]
        
    def writeOutput(self):
        assert isinstance(self.pc_plus_4.value, int) and isinstance(self.shifted_jump_adress.value, int)
        self.full_jump_adress.value = (self.pc_plus_4.value & 0xF0000000) | self.shifted_jump_adress.value