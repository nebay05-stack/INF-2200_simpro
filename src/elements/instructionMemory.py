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
        print("Minne-adresser i filen:", list(self.memory.keys()))
        self.Readaddres: Value = Value(0)

        # Output
        self.oppcode = Value(0)
        self.rs = Value(0)
        self.rd = Value(0)
        self.rt = Value(0)
        self.imidiat = Value(0) 
        self.function = Value(0)
        
    
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'instructionmemmory should have one inputs'
        self.Readaddres = inputs[0]


    def writeOutput(self):
        assert isinstance(self.Readaddres.value, int)

        instruction = self.memory.get(self.Readaddres.value, 0)

        self.oppcode.value = (instruction >> 26) & 0x3f 
        self.rs.value = (instruction >> 21) & 0x1f
        self.rt.value = (instruction >> 16) & 0x1f
        self.rd.value = (instruction >> 11) & 0x1f
        self.imidiat.value = (instruction >> 0) & 0xffff
        self.function.value = instruction & 0x3f

        print(f"PC: {self.Readaddres.value} | rs: {self.rs.value}, rt: {self.rt.value}")