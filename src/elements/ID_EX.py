from typing import List
from common import Value
from .cpuElement import CPUElement


class Id_ex(CPUElement):
    def __init__(self):
        #Inputs
        self.pc_adder_inp: Value = Value(0)
        self.read_data1_inp: Value = Value(0)
        self.read_data2_inp: Value = Value(0)
        self.signextend_inp: Value = Value(0)

        self.stall_signal: Value = Value(0)
        self.flush_signal: Value = Value(0)
        
        #Outputs
        self.pc_adder_out = Value(0)
        self.read_data1_out = Value(0)
        self.read_data2_out = Value(0)
        self.signextend_out = Value(0)
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 6, "id/ex should have 6 inputs"
        self.pc_adder_inp = inputs[0]
        self.read_data1_inp = inputs[1]
        self.read_data2_inp = inputs[2]
        self.signextend_inp = inputs[3]
        self.stall_signal = inputs[4]
        self.flush_signal = inputs[5]
        

    def writeOutput(self):
        assert isinstance(self.pc_adder_inp.value, int) and isinstance(self.read_data1_inp.value, int) and isinstance(self.read_data2_inp.value, int) and isinstance(self.signextend_inp.value, int) and isinstance(self.stall_signal.value, int) and isinstance(self.flush_signal.value, int)

        if self.flush_signal.value == 1:
            self.read_data1_out.value = 0
            self.read_data2_out.value = 0
            self.pc_adder_out.value = 0
        elif self.stall_signal.value == 1:
            pass
        else:
            self.pc_adder_out.value = self.pc_adder_inp.value
            self.read_data1_out.value = self.read_data1_inp.value
            self.read_data2_out.value = self.read_data2_inp.value
            self.signextend_out.value = self.signextend_inp.value
