from common import Value
from elements.cpuElement import CPUElement
from typing import List
from .dataMemory import DataMemory

class Sw(CPUElement):
    def __init__(self, data_memory):
        # Inputs
        self.value_a: Value = Value(0)
        self.value_b: Value = Value(0)
        
        # Output
        self.data_memory = data_memory

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, 'Sw should have two inputs'
        
        # Inputs
        self.value_a = inputs[0]
        self.value_b = inputs[1]
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.value_a.value, int) and isinstance(self.value_b.value, int)
        source_register_value = self.value_a & 0xffffffff
        target_adress = self.value_b.value & 0xffffffff # Convert to 32-bit (ignore overflow)
        self.data_memory.memory[target_adress] = source_register_value
        
        
        

