from typing import List
from common import Value
from .cpuElement import CPUElement


class If_id(CPUElement):
    def __init__(self):
        #Inputs
        self.pc_plus_4_inp: Value = Value(0)
        self.oppcode_inp: Value = Value(0)
        self.rs_inp: Value = Value(0)
        self.rd_inp: Value = Value(0)
        self.rt_inp: Value = Value(0)
        self.immidiat_inp: Value = Value(0)
        self.function_inp: Value = Value(0)
        self.jump_addres_inp: Value = Value(0)

        self.stall_signal: Value = Value(0)
        
        #Outputs
        self.pc_plus_4_out= Value(0)
        self.oppcode_out = Value(0)
        self.rs_out = Value(0)
        self.rd_out = Value(0)
        self.rt_out = Value(0)
        self.immidiat_out = Value(0) 
        self.function_out = Value(0)
        self.jump_addres_out = Value(0)
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 9, "if/id should have 10 inputs"
        self.pc_plus_4_inp = inputs[0]
        self.oppcode_inp = inputs[1]
        self.rs_inp = inputs[2]
        self.rt_inp = inputs[3]
        self.rd_inp = inputs[4]
        self.immidiat_inp = inputs[5]
        self.function_inp = inputs[6]
        self.jump_addres_inp = inputs[7]

        self.stall_signal = inputs[8]
      
        

    def writeOutput(self):
        assert isinstance(self.pc_plus_4_inp.value, int) and isinstance(self.oppcode_inp.value, int) and isinstance(self.stall_signal.value, int) 

        self.pc_plus_4_out.value = 0
        self.oppcode_out.value = 0
        self.rs_out.value = 0
        self.rd_out.value = 0
        self.rt_out.value = 0
        self.immidiat_out.value = 0
        self.function_out.value = 0
        self.jump_addres_out.value = 0
        
        if self.stall_signal.value == 0:
            pass
        else:
            self.pc_plus_4_out.value = self.pc_plus_4_inp.value
            self.oppcode_out.value = self.oppcode_inp.value
            self.rs_out.value = self.rs_inp.value
            self.rd_out.value = self.rd_inp.value
            self.rt_out.value = self.rt_inp.value
            self.immidiat_out.value = self.immidiat_inp.value
            self.function_out.value = self.function_inp.value
            self.jump_addres_out.value = self.jump_addres_inp.value