from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Addiu(CPUElement):
    def __init__(self):
        # Inputs
        self.value_a: Value = Value(0)
        self.value_b: Value = Value(0)
        
        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'Addiu should have two inputs'
        
        # Inputs
        self.value_a = inputs[0]
        self.value_b = inputs[1]

        assert isinstance(self.value_a.value, int) and isinstance(self.value_b.value, int)
        assert self.value_a.value >= 0 and self.value_b.value >= 0

    def writeOutput(self):
        # Output values
        assert isinstance(self.value_a.value, int) and isinstance(self.value_b.value, int)
        self.result.value = (self.value_a.value + self.value_b.value) & 0xffffffff # Convert to 32-bit (ignore overflow)
