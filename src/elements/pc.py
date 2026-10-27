'''
Code written for inf-2200, University of Tromso
'''

from common import Value
from elements.cpuElement import CPUElement
from typing import List

class PC(CPUElement):
    def __init__(self, baseaddr: int):
        self.baseaddr = baseaddr
        
        # Input
        self.incomingAddress: Value = Value(baseaddr)
        self.pc_write: Value = Value(0)
        
        # Output
        self.currentAddress: Value = Value(baseaddr)
    
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'PC should have 2 input'
        
        # Input
        self.incomingAddress = inputs[0]
        self.pc_write = inputs[1]
        self.incomingAddress.value = self.baseaddr
        
    def writeOutput (self):
        if self.pc_write.value == 1:
            self.currentAddress.value = self.incomingAddress.value