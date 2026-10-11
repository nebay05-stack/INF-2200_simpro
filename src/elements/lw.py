from common import Value
from elements.cpuElement import CPUElement
from typing import List

class Lw(CPUElement):
    def __init__(self, data_memory):
        # Inputs
        self.value_a: Value = Value(0)
        self.data_memory = data_memory

        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'Lw should have one inputs'
          
        # Inputs
        self.value_a = inputs[0]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.value_a.value, int) 
        target_adress = self.value_a.value & 0xffffffff
        adress_value = self.data_memory.memory.get(target_adress, 0)
        self.result.value = adress_value
        



        