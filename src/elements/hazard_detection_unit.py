from typing import List
from common import Value
from .cpuElement import CPUElement


class Hazard_detection(CPUElement):
    def __init__(self):
        #Inputs
        self.id_ex_RegWrite: Value = Value(0)
        self.muxregdist_result: Value = Value(0)
        self.ex_mem_RegWrite: Value = Value(0)
        self.ex_mem_reg_dst: Value = Value(0)
        
        

        self.if_id_rs: Value = Value(0)
        self.if_id_rt: Value = Value(0)
        self.branch_taken: Value = Value(0)
        self.id_ex_MemRead: Value = Value(0)
        #Outputs
        self.if_id_write= Value(1)
        self.pc_write = Value(1)
        self.id_ex_flush = Value(0)
        self.if_id_flush = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 8, "hazard detection should have 6 inputs"
        self.id_ex_RegWrite = inputs[0]
        self.muxregdist_result = inputs[1]
        self.ex_mem_RegWrite = inputs[2]
        self.ex_mem_reg_dst = inputs[3]
        self.if_id_rs = inputs[4]
        self.if_id_rt = inputs[5]
        self.branch_taken = inputs[6]
        self.id_ex_MemRead = inputs[7]
        

    def writeOutput(self):
        rs = self.if_id_rs.value
        rt = self.if_id_rt.value
       
        ex_hazard = (self.id_ex_RegWrite.value == 1 and self.muxregdist_result.value != 0 and self.muxregdist_result.value in (rs, rt))
        mem_hazard = (self.ex_mem_RegWrite.value == 1 and self.ex_mem_reg_dst.value != 0 and self.ex_mem_reg_dst.value in (rs, rt))

        stall = ex_hazard or mem_hazard

        if stall:
            self.pc_write.value = 0
            self.if_id_write.value = 0
            self.id_ex_flush.value = 1
        else:
            self.pc_write.value = 1
            self.if_id_write.value = 1
            self.id_ex_flush.value = 0

        if self.branch_taken.value == 1 and not stall:
            self.if_id_flush.value = 1
        else:
            self.if_id_flush.value = 0

    
           

    

       
        
