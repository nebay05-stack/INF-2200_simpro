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
        self.reg_dst_inp: Value = Value(0)

        self.controll_signal_inp: dict[str, Value] = {
            'MemtoReg': Value(0), 
            'MemRead': Value(0), 
            'MemWrite': Value(0), 
            'RegWrite': Value(0)
        }
        
        #Outputs
        self.adder_result_out= Value(0)
        self.zero_result_out = Value(0)
        self.alu_result_out = Value(0)
        self.readdata_2_out = Value(0)
        self.reg_dst_out = Value(0)

        self.controll_signal_out: dict[str, Value] ={
            k: Value(0) for k in self.controll_signal_inp
        }

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) >= 5, "ex/mem should have 6 inputs"
        self.adder_result_inp = inputs[0]
        self.zero_result_inp = inputs[1]
        self.alu_result_inp = inputs[2]
        self.readdata_2_inp = inputs[3]
        self.reg_dst_inp = inputs[4]

        controll_keys = list(self.controll_signal_inp.keys())
        for i, key in enumerate(controll_keys):
            if len(inputs) > 5 + i:
                self.controll_signal_inp[key] = inputs[5 + i]
        

    def writeOutput(self):
        assert isinstance(self.adder_result_inp.value, int) and isinstance(self.zero_result_inp.value, int) and isinstance(self.alu_result_inp.value, int) and isinstance(self.read_data2_inp.value, int) 

        
        self.adder_result_out.value = self.adder_result_inp.value
        self.zero_result_out.value = self.zero_result_inp.value
        self.alu_result_out.value = self.alu_result_inp.value
        self.readdata_2_out.value = self.readdata_2_inp.value
        self.reg_dst_out.value = self.reg_dst_inp.value

        for key in self.controll_signal_inp:
            self.controll_signal_out[key].value = self.controll_signal_inp[key].value
            