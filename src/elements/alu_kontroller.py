from typing import List
from common import Value
from .cpuElement import CPUElement

class AluController(CPUElement):
    def __init__(self):
        # Inputs 
        self.alu_op = Value(0)
        self.function = Value(0)
        
        # Output
        self.alu_control_out = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 2, "alucontroller should have 2 inputs"
        self.alu_op = inputs[0]
        self.function = inputs[1]

    def writeOutput(self):
        op = self.alu_op.value
        fn = self.function.value
        assert isinstance(op, int) and isinstance(fn, int)

        if op == 0b00:
            self.alu_control_out.value = 0b0010
        elif op == 0b01:
            self.alu_control_out.value = 0b0110
        elif op == 0b11: #lui
            self.alu_control_out.value = 0b1111
            
        #ALUOp er 10 (R-type) se på fuction kode for spesifik opperajon
        elif op == 0b10:
            if fn == 0b100000 or fn == 0b100001:     #add eller addu
                self.alu_control_out.value = 0b0010
            elif fn == 0b100010 or fn == 0b100011:   #sub eller subu
                self.alu_control_out.value = 0b0110
            elif fn == 0b100100:   # and[cite: 1]
                self.alu_control_out.value = 0b0000
            elif fn == 0b100101:   # or[cite: 1]
                self.alu_control_out.value = 0b0001
            elif fn == 0b101010:   # slt (set on less than)[cite: 1]
                self.alu_control_out.value = 0b0111
            elif fn == 0b100111:   # nor
                self.alu_control_out.value = 0b1100
            else:
                self.alu_control_out.value = 0b0000
        else:
            self.alu_control_out.value = 0b0000
        