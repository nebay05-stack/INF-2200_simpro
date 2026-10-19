from typing import List
from common import Value
from .cpuElement import CPUElement


class If_id(CPUElement):
    def __init__(self):
        #Inputs
        self.pc_adder_inp: Value = Value(0)
        self.instruction_inp: Value = Value(0)

        self.stall_signal: Value = Value(0)
        self.flush_signal: Value = Value(0)
        
        #Outputs
        self.pc_adder_out= Value(0)
        self.instruction_out = Value(0)
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 4, "if/id should have 4 inputs"
        self.pc_adder_inp = inputs[0]
        self.instruction_inp = inputs[1]
        self.stall_signal = inputs[2]
        self.flush_signal = inputs[3]
        

    def writeOutput(self):
        assert isinstance(self.pc_adder_inp.value, int) and isinstance(self.instruction_inp.value, int) and isinstance(self.stall_signal.value, int) and isinstance(self.flush_signal.value, int)

        if self.flush_signal.value == 1:
            self.instruction_out.value = 0
            self.pc_adder_out.value = 0
        elif self.stall_signal.value == 1:
            pass
        else:
            self.pc_adder_out.value = self.pc_adder_inp.value
            self.instruction_out.value = self.instruction_inp.value