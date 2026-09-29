from common import Value
from elements.cpuElement import CPUElement
from typing import List


class Controll_unit(CPUElement):
    def __init__(self):
        # Inputs
        self.value_a: Value = Value(0)
        self.value_b: Value = Value(0)
        
        # Output
        self.result = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'controll_unit should have one inputs'
        oppcode = inputs[0].value
        
        if oppcode == 0:
            self.Regwight = 1, self.Alusec = 0, self.Memtoreg = 0, self.Regwrite = 1, self.Memread = 0,
            self.Memwrite = 0, self.Branch = 0, self.Aluop = 10


        
        
    def writeOutput(self):
        # Output values
        assert isinstance(self.value_a.value, int) and isinstance(self.value_b.value, int)
        self.result.value = (self.value_a.value + self.value_b.value) & 0xffffffff # Convert to 32-bit (ignore overflow)
