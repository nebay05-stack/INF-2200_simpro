from typing import List
from common import Value
from .cpuElement import CPUElement


class Id_ex(CPUElement):
    def __init__(self):
        #Inputs
        self.pc_plus_4_inp: Value = Value(0)
        self.readdata_1_inp: Value = Value(0)
        self.readdata_2_inp: Value = Value(0)
        self.signextend_inp: Value = Value(0)
        self.rt_inp: Value = Value(0)
        self.rd_inp: Value = Value(0)

        self.flush_signal: Value = Value(0)
        self.function_inp: Value = Value(0)


        self.controll_signal_inp: dict[str, Value] = {
            'RegDst': Value(0), 'Branch': Value(0),
            'MemtoReg': Value(0), 'MemRead': Value(0), 
            'ALUOp': Value(0),'MemWrite': Value(0), 
            'ALUSrc': Value(0), 'RegWrite': Value(0)
        }
        
        #Outputs
        self.pc_plus_4_out = Value(0)
        self.readdata_1_out = Value(0)
        self.readdata_2_out = Value(0)
        self.signextend_out = Value(0)
        self.rt_out = Value(0)
        self.rd_out = Value(0)
        self.function_out = Value(0)

        self.controll_signal_out: dict[str, Value] ={
            k: Value(0) for k in self.controll_signal_inp
        }
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) >= 9, "id/ex should have 9 inputs"
        self.pc_plus_4_inp = inputs[0]
        self.readdata_1_inp = inputs[1]
        self.readdata_2_inp = inputs[2]
        self.signextend_inp = inputs[3]
        self.rt_inp = inputs[4]
        self.rd_inp = inputs[5]
        self.flush_signal = inputs[6]
        self.function_inp = inputs[7]

        controll_keys = list(self.controll_signal_inp.keys())
        for i, key in enumerate(controll_keys):
            if len(inputs) > 8 + i:
                self.controll_signal_inp[key] = inputs[8 + i]


        
    def writeOutput(self):
        assert isinstance(self.pc_plus_4_inp.value, int) and \
              isinstance(self.readdata_1_inp.value, int) and \
                isinstance(self.readdata_2_inp.value, int) and isinstance(self.signextend_inp.value, int) and isinstance(self.flush_signal.value, int)

        if self.flush_signal.value == 1:
            self.readdata_1_out.value = 0
            self.readdata_2_out.value = 0
            self.pc_plus_4_out.value = 0
            self.signextend_out.value = 0
            self.rt_out.value = 0
            for key in self.controll_signal_out:
                self.controll_signal_out[key].value = 0
        else:
            self.pc_plus_4_out.value = self.pc_plus_4_inp.value
            self.readdata_1_out.value = self.readdata_1_inp.value
            self.readdata_2_out.value = self.readdata_2_inp.value
            self.rt_out.value = self.rt_inp.value
            self.rd_out.value = self.rd_inp.value
            self.signextend_out.value = self.signextend_inp.value
            self.function_out.value = self.function_inp.value

            for key in self.controll_signal_inp:
                self.controll_signal_out[key].value = self.controll_signal_inp[key].value
