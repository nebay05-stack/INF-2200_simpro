'''
Implements CPU element for Instruction Memory in MEM stage.

Code written for inf-2200, University of Tromso
'''

from elements.memory import Memory
from common import Value
from typing import List

class InstructionMemory(Memory):
    def __init__(self, filename: str):
        Memory.__init__(self, filename)
        self.Readaddres: Value = Value(0)

        # Output
        self.result = Value(0)
        
    
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'instructionmemmory should have two inputs'
        self.Readaddres = inputs[0]


    def writeOutput(self):
        assert isinstance(self.Readaddres.value, int)
        self.result.value = self.memory.get(self.Readaddres.value, 0)
        
