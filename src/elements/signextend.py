import common  
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
class Shiftleft(CPUElement):
    def __init__(self):
        # Inputs
        self.value_a: Value = Value(0)
        
        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'shiftleft should have one inputs'
        
        self.value_a = inputs[0]
        
    def writeOutput(self):
        assert isinstance(self.value_a.value, int) 
        self.result.value = (self.value_a.value << 2) & 0xFFFFFFFF

        