from typing import List
from common import Value
from .cpuElement import CPUElement


class Hazard_detection(CPUElement):
    def __init__(self):
        #Inputs
        self.id_ex_MemRead: Value = Value(0)
        self.id_ex_register_rt: Value = Value(0)

        self.if_id_rs: Value = Value(0)
        self.if_id_rt: Value = Value(0)
        
        #Outputs
        self.if_id_write= Value(1)
        self.pc_write = Value(1)
        self.id_ex_flush = Value(0)
    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 4, "hazard detection should have 4 inputs"
        self.id_ex_MemRead = inputs[0]
        self.id_ex_register_rt = inputs[1]
        self.if_id_rs = inputs[2]
        self.if_id_rt = inputs[3]
        

    def writeOutput(self):
        assert isinstance(self.id_ex_MemRead.value, int) and isinstance(self.id_ex_register_rt.value, int) and isinstance(self.if_id_rs.value, int) and isinstance(self.if_id_rt.value, int)

        self.pc_write.value = 1
        self.if_id_write.value = 1
        self.id_ex_flush.value = 0

        if self.id_ex_MemRead.value == 1:
            if (self.id_ex_register_rt.value == self.if_id_rt.value) or (self.id_ex_register_rt.value == self.if_id_rs.value):
                self.pc_write.value = 0
                self.if_id_write.value = 0
                self.id_ex_flush.value = 1
        
