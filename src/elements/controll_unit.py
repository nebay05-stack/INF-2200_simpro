from common import Value
from elements.cpuElement import CPUElement
from typing import List


class Controller(CPUElement):
    def __init__(self):
        # Inputs
        self.oppcode = Value(0)
        
        # Output
        self.RegDst: Value = Value(0)
        self.Branch: Value = Value(0)
        self.MemRead: Value = Value(0)
        self.MemtoReg: Value = Value(0)
        self.ALUOp: Value = Value(0)
        self.MemWrite: Value = Value(0)
        self.ALUSrc: Value = Value(0)
        self.RegWrite: Value = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'controller should have one inputs'

        oppcode = inputs[0].value

        
    def writeOutput(self):

        if self.oppcode.value == 0: #add signalene
            self.RegDst.value = 1
            self.ALUSrc.value = 0
            self.RegWrite.value = 1
            self.ALUOp.value = 10
        elif self.oppcode.value == 8 or self.oppcode.value == 9: #addi og addiu signalene
            self.RegDst.value = 0
            self.ALUSrc.value = 1
            self.RegWrite.value = 1
            self.ALUOp.value = 10
            if self.result #her skal overflow håndteres for å hondtere foskjellen mellom addi og addiu resultatet
        elif self.oppcode.value == 35: #lw signalene
            self.RegDst.value = 0
            self.ALUSrc.value = 1
            self.MemtoReg.value = 1
            self.RegWrite.value = 1
            self.MemRead.value = 1
            self.ALUOp.value = 00
        elif self.oppcode.value == 43: #sw signalene
            self.ALUSrc.value = 1
            self.MemWrite.value = 1
            self.ALUOp.value = 00 

