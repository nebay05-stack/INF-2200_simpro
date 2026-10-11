from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Lui(CPUElement):
    def __init__(self):
        # Inputs
        self.value_a: Value = Value(0)

        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'lui should have one inputs'
          
        # Inputs
        self.value_a = inputs[0]
        
        
    def writeOutput(self):
        assert isinstance(self.value_a.value, int) 
        self.result.value = (self.value_a.value << 16) & 0xffff0000