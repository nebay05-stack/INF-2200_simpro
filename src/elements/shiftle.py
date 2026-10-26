from typing import List
from common import Value
from .cpuElement import CPUElement
import common


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
        signed_value = common.fromUnsignedWordToSignedWord(self.value_a.value)

        self.result.value = (signed_value << 2) & 0xFFFFFFFF