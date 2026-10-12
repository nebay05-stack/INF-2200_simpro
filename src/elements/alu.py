from typing import List
from common import Value
from .cpuElement import CPUElement

class Alu(CPUElement):
    def __init__(self):
        # Inputs
        self.source_1: Value = Value(0)
        self.source_2: Value = Value(0)
        self.alu_control: Value = Value(0)
        
        # Outputs
        self.result: Value = Value(0)
        self.zero: Value = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 3, "alu should have 3 inputs"
        self.source_1 = inputs[0]
        self.source_2 = inputs[1]
        self.alu_control = inputs[2]

    def writeOutput(self):
        v1 = self.source_1.value
        v2 = self.source_2.value
        four_bit = self.alu_control.value

        assert isinstance(self.source_1.value, int) and isinstance(self.source_2.value, int)

        res = 0

        #utfør operasjon basert på alu control-input fra tabellen
        if four_bit == 0b0010: #addisjon
            res = self.source_1.value + self.source_2.value
        elif four_bit == 0b0110: #subtraksjon
            res = (self.source_1.value - self.source_2.value) & 0xffffffff
        elif four_bit == 0b0000: #and
            res = (self.source_1.value & self.source_2.value) & 0xffffffff
        elif four_bit == 0b0001: #or
            res = (self.source_1.value | self.source_2.value) & 0xffffffff
        elif four_bit == 0b0111: #slt
            res = 1 if self.source_1.value < self.source_2.value else 0
        elif four_bit == 0b1100:
            res = ~(self.source_1.value | self.source_2.value) & 0xffffffff
        elif four_bit == 0b1111:
            res = (v2 << 16) & 0xFFFFFFFF
        else:
            res = 0 
            

        self.result.value = res 
        if res == 0:
            self.zero.value = 1
        else:
            self.zero.value = 0