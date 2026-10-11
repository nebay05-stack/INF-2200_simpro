from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Break_op(CPUElement):
    def __init__(self):
        # Inputy
        self.break_signal: Value = Value(0)
        
        # Output
        self.full_stop = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'break should have one inputs'
        
        # Inputs
        self.break_signal = inputs[0]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.break_signal.value, int) 
        if self.break_signal.value == 13:
            self.full_stop.value = 1
        else:
            self.full_stop.value = 0
        