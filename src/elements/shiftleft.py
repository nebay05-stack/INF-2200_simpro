from elements.cpuElement import CPUElement
from typing import List
class Shiftleft(CPUElement):
    def __init__(self):
        #Input
        self.input_val: Value = Value(0)

        #Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'shiftLeft2 should have one input'
        self.input_val = inputs[0]
        
    def writeOutput(self):
        assert isinstance(self.input_val.value, int)
        self.result.value = (self.input_val.value << 2) & 0xFFFFFFFF