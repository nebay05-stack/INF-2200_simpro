'''
Code written for inf-2200, University of Tromso
'''
from common import Break, Overflow
from elements.pc import PC
from elements.add import Add
from elements.break_op import Break_op
from elements.break_op import Break_op
from elements.mux import Mux
from elements.controll_unit import Controller
from elements.registerFile import RegisterFile
from elements.instructionMemory import InstructionMemory
from elements.dataMemory import DataMemory
from elements.constant import Constant
from elements.signextend import Signextend, Shiftleft
from elements.alu_kontroller import AluController
from elements.alu import Alu
from elements.jump_slicer import JumpSlicer



class MIPSSimulator():
    '''Main class for MIPS pipeline simulator.

    Provides the main method tick(), which runs pipeline
    for one clock cycle.

    '''

    def __init__(self, memoryFileName: str):
        self.nCycles = 0  # Used to hold number of clock cycles spent executing instructions

        self.dataMemory = DataMemory(memoryFileName)
        self.instructionMemory = InstructionMemory(memoryFileName)
        self.registerFile = RegisterFile()
        self.constant3 = Constant(3)
        self.constant4 = Constant(4)
        self.controller = Controller()
        self.muxPCSrc = Mux()
        self.muxRegDst = Mux()
        self.muxMemtoReg = Mux()
        self.muxALUSrc = Mux()
        self.muxJump = Mux()
        self.adder = Add()
        self.branch_adder = Add()
        self.signextend = Signextend()
        self.shiftleft = Shiftleft()
        self.shiftleft_jump = Shiftleft()
        self.jump_slicer = JumpSlicer()
        self.alu = Alu()
        self.alu_kontroller = AluController()
        self.brake = Break_op()
        self.pc = PC(self.startAddress())

        self.elements = [
            self.pc, 
            self.constant3, 
            self.constant4, 
            self.adder, 
            self.instructionMemory, 
            self.controller, 
            self.signextend, 
            self.shiftleft,
            self.shiftleft_jump,
            self.jump_slicer, 
            self.branch_adder, 
            self.muxRegDst, 
            self.muxALUSrc, 
            self.alu_kontroller, 
            self.alu, 
            self.dataMemory, 
            self.muxMemtoReg, 
            self.muxPCSrc,
            self.muxJump, 
            self.brake,
            self.registerFile  
        ]
        self._connectCPUElements()

    def _connectCPUElements(self):
        self.constant3.connectInputs([])
        self.constant4.connectInputs([])
        self.pc.connectInputs([self.muxJump.output])
        self.adder.connectInputs([self.pc.currentAddress, self.constant4.constantValue])
        self.muxPCSrc.connectInputs([self.adder.result, self.branch_adder.result, self.controller.Branch])
        self.instructionMemory.connectInputs([self.pc.currentAddress])
        self.controller.connectInputs([self.instructionMemory.oppcode])
        self.brake.connectInputs([self.instructionMemory.oppcode ,self.instructionMemory.function])
        self.shiftleft.connectInputs([self.signextend.result])
        self.branch_adder.connectInputs([self.adder.result, self.shiftleft.result])

        self.shiftleft_jump.connectInputs([self.instructionMemory.jump_addres])
        self.jump_slicer.connectInputs([self.adder.result, self.shiftleft_jump.result])
        self.muxJump.connectInputs([self.muxPCSrc.output, self.jump_slicer.full_jump_adress, self.controller.Jump])
        
        self.muxRegDst.connectInputs([self.instructionMemory.rt, self.instructionMemory.rd, self.controller.RegDst])

        self.registerFile.connectInputs([self.instructionMemory.rs, self.instructionMemory.rt, self.muxRegDst.output, self.muxMemtoReg.output, self.controller.RegWrite])

        self.signextend.connectInputs([self.instructionMemory.imidiat])

        self.muxALUSrc.connectInputs([self.registerFile.readdata_2, self.signextend.result, self.controller.ALUSrc])
        self.alu_kontroller.connectInputs([self.controller.ALUOp, self.instructionMemory.function])

        self.alu.connectInputs([self.registerFile.readdata_1, self.muxALUSrc.output, self.alu_kontroller.alu_control_out])
        self.dataMemory.connectInputs([self.alu.result, self.registerFile.readdata_2, self.controller.MemRead, self.controller.MemWrite])
        self.muxMemtoReg.connectInputs([self.alu.result, self.dataMemory.readdata, self.controller.MemtoReg])
        
        #self. imidiat bittene


    def startAddress(self):
        '''
        Returns first instruction from instruction memory
        '''
        return next(iter(sorted(self.instructionMemory.memory.keys())))

    def clockCycles(self):
        '''Returns the number of clock cycles spent executing instructions.'''

        return self.nCycles

    def memory(self):
        '''Returns dictionary, mapping memory addresses to data, holding
        data memory after instructions have finished executing.'''

        return self.dataMemory.memory

    def registers(self):
        '''Returns dictionary, mapping register numbers to data, holding
        register file after instructions have finished executing.'''

        return self.registerFile.register

    def printDataMemory(self):
        self.dataMemory.printAll()

    def printRegisterFile(self):
        self.registerFile.printAll()

    def tick(self):
        '''Execute one clock cycle of pipeline.'''
        
        self.nCycles += 1

        for elem in self.elements:
            elem.writeOutput()

            if elem == self.instructionMemory:
                self.registerFile.read_register()

            if elem == self.alu:
                opcode = self.instructionMemory.oppcode.value
                is_branch = self.controller.Branch.value == 1
                zero = self.alu.zero.value


                branch_taken = 0
                if is_branch:
                    if opcode == 4 and zero == 1: #beq
                        branch_taken = 1
                    elif opcode == 5 and zero == 0: #bne
                        branch_taken = 1

                self.muxPCSrc.controlSignal.value = branch_taken

                is_jump = 1 if opcode == 2 else 0
                self.muxJump.controlSignal.value = is_jump

        
        function = self.instructionMemory.function.value

        r_type = (opcode == 0 and (function == 0b100010 or function == 0b100000))
        i_type = opcode == 8
                            
        if r_type or i_type:
            if self.alu.overflow.value == 1:
                raise Overflow("overflow detected")
        
        if self.brake.full_stop.value == 1:
            raise Break("Break instruction encountered")
        
