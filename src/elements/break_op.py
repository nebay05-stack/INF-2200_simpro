from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Break_op(CPUElement):
    def __init__(self):
        # Inputy
        self.oppcode: Value = Value(0)
        self.funtion: Value = Value(0)
        
        # Output
        self.full_stop = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'break should have two inputs'
        
        # Inputs
        self.oppcode = inputs[0]
        self.funtion = inputs[1]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.oppcode.value, int) and isinstance(self.funtion.value, int) 
        if (self.oppcode.value == 0) and (self.funtion.value == 13):
            self.full_stop.value = 1
        else:
            self.full_stop.value = 0
        