from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Signextend(CPUElement):
    def __init__(self):
        # Inputs
        self.adress: Value = Value(0)
        
        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'signextend should have one inputs'
        
        # Inputs
        self.adress = inputs[0]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.adress.value, int) 
        if self.adress.value & 0x8000:
            self.result.value = self.adress.value | 0xFFFF0000
        else:
            self.result.value = self.adress.value & 0xFFFF


        