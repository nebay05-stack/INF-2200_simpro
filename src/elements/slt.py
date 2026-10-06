from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Slt(CPUElement):
    def __init__(self):
        # Inputs
        self.value_a: Value = Value(0)
        self.value_b: Value = Value(0)
        
        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'Slt should have two inputs'
        
        # Inputs
        self.value_a = inputs[0]
        self.value_b = inputs[1]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.value_a.value, int) and isinstance(self.value_b.value, int)
        if (self.value_a.value < self.value_b.value):
            self.result.value = 1
        