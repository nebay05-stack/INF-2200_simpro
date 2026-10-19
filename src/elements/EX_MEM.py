from typing import List
from common import Value
from .cpuElement import CPUElement


class Ex_mem(CPUElement):
    def __init__(self):
        #Inputs
        self.adder_result_inp: Value = Value(0)
        self.zero_result_inp: Value = Value(0)
        self.alu_result_inp: Value = Value(0)
        self.read_data2_inp: Value = Value(0)

        self.stall_signal: Value = Value(0)
        self.flush_signal: Value = Value(0)
        
        #Outputs
        self.adder_result_out= Value(0)
        self.zero_result_out = Value(0)
        self.alu_result_out = Value(0)
        self.read_data2_out = Value(0)
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 5, "ex/mem should have 5 inputs"
        self.adder_result_inp = inputs[0]
        self.zero_result_inp = inputs[1]
        self.alu_result_inp = inputs[2]
        self.read_data2_inp = inputs[3]
        self.stall_signal = inputs[4]
        self.flush_signal = inputs[5]
        

    def writeOutput(self):
        assert isinstance(self.adder_result_inp.value, int) and isinstance(self.zero_result_inp.value, int) and isinstance(self.alu_result_inp.value, int) and isinstance(self.read_data2_inp.value, int) and isinstance(self.stall_signal.value, int) and isinstance(self.flush_signal.value, int)

        if self.flush_signal.value == 1:
            self.adder_result_out.value = 0
            self.zero_result_out.value = 0
            self.alu_result_out.value = 0
            self.read_data2_out.value = 0
        elif self.stall_signal.value == 1:
            pass
        else:
            self.adder_result_out.value = self.adder_result_inp.value
            self.zero_result_out.value = self.zero_result_inp.value
            self.alu_result_out.value = self.alu_result_inp.value
            self.read_data2_out.value = self.read_data2_inp.value