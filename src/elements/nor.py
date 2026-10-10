from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Nor(CPUElement):
    def __init__(self):
        # Inputs
        self.value_a: Value = Value(0)
        self.value_b: Value = Value(0)
        
        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'Nor should have two inputs'
        
        # Inputs
        self.value_a = inputs[0]
        self.value_b = inputs[1]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.value_a.value, int) and isinstance(self.value_b.value, int)
        or_result = self.value_a.value | self.value_b.value

        not_or_result = ~or_result

        self.result.value = not_or_result & 0xffffffff # Convert to 32-bit (ignore overflow)
