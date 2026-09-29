from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Lw(CPUElement):
    def __init__(self):
        # Inputs
        self.value_a: Value = Value(0)
        self.register: Value = Value(0)
        
        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'Lw should have two inputs'
          
        # Inputs
        self.value_a = inputs[0]
        self.register = inputs[1]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.value_a.value, int) and isinstance(self.register.value, int)
        