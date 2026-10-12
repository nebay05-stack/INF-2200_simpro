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
        self.Jump: Value = Value(0)
        self.Break: Value = Value(0)

    def connectInputs(self, inputs: List[Value]):
        assert len(inputs) == 1, 'controller should have one inputs'

        self.oppcode = inputs[0]

        
    def writeOutput(self):

        self.RegDst.value = 0
        self.Branch.value = 0
        self.MemRead.value = 0
        self.MemtoReg.value = 0
        self.ALUOp.value = 0
        self.MemWrite.value = 0
        self.ALUSrc.value = 0
        self.RegWrite.value = 0
        self.Jump.value = 0
        self.Break.value = 0

        oppcode = self.oppcode.value

        if oppcode == 0: #alle r-type instruksjoner
            self.RegDst.value = 1
            self.ALUSrc.value = 0
            self.RegWrite.value = 1
            self.ALUOp.value = 0b10
        elif oppcode == 8 or oppcode == 9: #addi og addiu
            self.RegDst.value = 0
            self.ALUSrc.value = 1
            self.RegWrite.value = 1
            self.ALUOp.value = 0b00
        elif oppcode == 35: #lw
            self.RegDst.value = 0
            self.ALUSrc.value = 1
            self.MemtoReg.value = 1
            self.RegWrite.value = 1
            self.MemRead.value = 1
            self.ALUOp.value = 0b00
            
        elif oppcode == 43: #sw
            self.ALUSrc.value = 1
            self.MemWrite.value = 1
            self.ALUOp.value = 0b00
        elif oppcode == 4: #beq
            self.Branch.value = 1
            self.ALUOp.value = 1 
            self.ALUOp.value = 0b01 
        elif oppcode == 5: #bne
            self.Branch.value = 1 
            self.ALUOp.value = 1 
            self.ALUOp.value = 0b01 
        elif oppcode == 2: #j
            self.Jump.value = 1
        elif oppcode == 15: #lui
            self.RegDst.value = 0
            self.ALUSrc.value = 1
            self.RegWrite.value = 1
            self.ALUOp.value = 0b11
