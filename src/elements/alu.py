from typing import List
from common import Value, Overflow
from .cpuElement import CPUElement
Max_int_value = 2147483647
Min_int_value = -2147483648

class Alu(CPUElement):
    def __init__(self):
        #Inputs
        self.source_1: Value = Value(0)
        self.source_2: Value = Value(0)
        self.alu_control: Value = Value(0)
        
        #Outputs
        self.result= Value(0)
        self.zero = Value(0)
        self.overflow = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 3, "alu should have 3 inputs"
        self.source_1 = inputs[0]
        self.source_2 = inputs[1]
        self.alu_control = inputs[2]

    def writeOutput(self):
        assert isinstance(self.source_1.value, int) and isinstance(self.source_2.value, int)
        four_bit = self.alu_control.value
        
        val_1 = self.source_1.value
        val_2 = self.source_2.value

        res_1 = 0
        res = 0
        self.overflow.value = 0


        #utfør operasjon basert på alu control input fra tabellen
        if four_bit == 0b0010: #add
            res = (val_1 + val_2) & 0xffffffff
            if ((val_1 & 0x80000000) == (val_2 & 0x80000000)) and ((val_1 & 0x80000000) != (res & 0x80000000)):
                self.overflow.value = 1
        elif four_bit == 0b0110: #sub
            res = (val_1 - val_2) & 0xffffffff
            if ((val_1 & 0x80000000) != (val_2 & 0x80000000)) and ((val_1 & 0x80000000) != (res & 0x80000000)):
                self.overflow.value = 1
        elif four_bit == 0b0000: #and
            res = (self.source_1.value & self.source_2.value) & 0xffffffff
        elif four_bit == 0b0001: #or
            res = (self.source_1.value | self.source_2.value) & 0xffffffff
        elif four_bit == 0b0111: #slt
            if self.source_1.value < self.source_2.value:
                res = 1
            else:
                res = 0
        elif four_bit == 0b1100:
            res = ~(self.source_1.value | self.source_2.value) & 0xffffffff
        elif four_bit == 0b1111:
            res = (self.source_2.value << 16) & 0xFFFFFFFF
        else:
            res = 0 

    
        self.result.value = res 
        if res == 0:
           self.zero.value = 1
        else:
           self.zero.value = 0