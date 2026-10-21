'''
Code written for inf-2200, University of Tromso
'''
from common import Break, Overflow, Value
from elements.pc import PC
from elements.IF_ID import If_id
from elements.ID_EX import Id_ex
from elements.EX_MEM import Ex_mem
from elements.MEN_WB import Mem_wb
from elements.hazard_detection_unit import Hazard_detection
from elements.add import Add
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
        self.if_id_register = If_id()
        self.id_ex_register = Id_ex()
        self.ex_mem_register = Ex_mem()
        self.mem_wb_register = Mem_wb()
        self.hazard_detection = Hazard_detection()

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
        self.pc.connectInputs([self.muxJump.output, self.hazard_detection.pc_write])
        self.adder.connectInputs([self.pc.currentAddress, self.constant4.constantValue])
        self.instructionMemory.connectInputs([self.pc.currentAddress])


        self.if_id_register.connectInputs([self.adder.result, self.instructionMemory.oppcode, self.instructionMemory.rs, self.instructionMemory.rt, 
                                           self.instructionMemory.rd, self.instructionMemory.imidiat, self.instructionMemory.function, self.instructionMemory.jump_addres, self.hazard_detection.if_id_write])
        self.controller.connectInputs([self.instructionMemory.oppcode])
        self.hazard_detection.connectInputs([self.id_ex_register.controll_signal_out['MemRead'], self.id_ex_register.rt_out, self.if_id_register.rs_out, self.if_id_register.rt_out])

        self.registerFile.connectInputs([self.if_id_register.rs_out, self.if_id_register.rt_out, self.mem_wb_register.reg_dest_out, self.muxMemtoReg.output, self.mem_wb_register.controll_signal_out['RegWrite']])
        self.signextend.connectInputs([self.if_id_register.immidiat_out])
        self.id_ex_register.connectInputs([self.if_id_register.pc_plus_4_out, self.registerFile.readdata_1, self.registerFile.readdata_2, 
                                           self.signextend.result, self.if_id_register.rt_out, self.if_id_register.rd_out, self.hazard_detection.id_ex_flush, 
                                           self.if_id_register.function_out, self.controller.RegDst, self.controller.Branch, self.controller.MemtoReg, self.controller.MemRead, 
                                           self.controller.ALUOp, self.controller.MemWrite, self.controller.ALUSrc, self.controller.RegWrite])
        self.ex_mem_register.connectInputs([self.id_ex_register.pc_plus_4_out, self.alu.zero, self.alu.result, self.id_ex_register.readdata_2_out, 
                                            self.muxRegDst.output, self.id_ex_register.controll_signal_out['MemtoReg'], self.id_ex_register.controll_signal_out['MemRead'], 
                                            self.id_ex_register.controll_signal_out['MemWrite'], self.id_ex_register.controll_signal_out['RegWrite']])
        self.dataMemory.connectInputs([self.ex_mem_register.alu_result_out, self.ex_mem_register.readdata_2_out, self.ex_mem_register.controll_signal_out['MemRead'], self.ex_mem_register.controll_signal_out['MemWrite']])
        self.muxRegDst.connectInputs([self.id_ex_register.rt_out, self.id_ex_register.rd_out, self.id_ex_register.controll_signal_out['RegDst']])
        self.muxALUSrc.connectInputs([self.id_ex_register.readdata_2_out, self.id_ex_register.signextend_out, self.id_ex_register.controll_signal_out['ALUSrc']])

        self.mem_wb_register.connectInputs([self.dataMemory.readdata, self.ex_mem_register.alu_result_out, self.ex_mem_register.reg_dst_out, self.ex_mem_register.controll_signal_out['MemtoReg'], 
                                            self.ex_mem_register.controll_signal_out['RegWrite']])
        self.muxMemtoReg.connectInputs([self.mem_wb_register.alu_result_out, self.mem_wb_register.read_data_out, self.mem_wb_register.controll_signal_out['MemtoReg']])

        self.alu.connectInputs([self.id_ex_register.readdata_1_out, self.muxALUSrc.output, self.alu_kontroller.alu_control_out])
        self.alu_kontroller.connectInputs([self.id_ex_register.controll_signal_out['ALUOp'], self.id_ex_register.function_out])
        self.muxPCSrc.connectInputs([self.adder.result, self.branch_adder.result, self.id_ex_register.controll_signal_out['Branch']])
        
        self.brake.connectInputs([self.instructionMemory.oppcode ,self.instructionMemory.function])
        self.shiftleft.connectInputs([self.id_ex_register.signextend_out])
        self.branch_adder.connectInputs([self.id_ex_register.pc_plus_4_out, self.shiftleft.result])

        self.shiftleft_jump.connectInputs([self.if_id_register.jump_addres_out])
        self.jump_slicer.connectInputs([self.if_id_register.pc_plus_4_out, self.shiftleft_jump.result])
        self.muxJump.connectInputs([self.muxPCSrc.output, self.jump_slicer.full_jump_adress, self.controller.Jump])



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

        self.constant4.writeOutput()

        if self.nCycles > 1:
            self.pc.writeOutput()

        self.adder.writeOutput()
        self.instructionMemory.writeOutput()
        self.if_id_register.writeOutput()
        self.controller.writeOutput()
        
        self.hazard_detection.writeOutput()


        self.registerFile.read_register()
        self.signextend.writeOutput()
        self.shiftleft_jump.writeOutput()
        self.jump_slicer.writeOutput()
        self.id_ex_register.writeOutput()
        
        self.shiftleft.writeOutput()
        self.branch_adder.writeOutput()
        self.muxALUSrc.writeOutput()
        self.muxRegDst.writeOutput()
        self.alu_kontroller.writeOutput()
        self.alu.writeOutput()
    
        is_branch = self.id_ex_register.controll_signal_out['Branch'].value == 1
        zero = self.alu.zero.value
        opcode = self.if_id_register.oppcode_out.value

        branch_taken = 0

        if is_branch:
            if opcode == 4 and zero == 1:
                branch_taken = 1
            elif opcode == 5 and zero == 0:            
                branch_taken = 1
            else:
                branch_taken = 0


        self.muxPCSrc.controlSignal.value = branch_taken
        self.muxPCSrc.writeOutput()            

        if self.controller.Jump.value == 1:
            is_jump = 1
        else:
            is_jump = 0
        self.muxJump.controlSignal.value = is_jump
        self.muxJump.writeOutput()


        
        self.ex_mem_register.writeOutput()
        self.dataMemory.writeOutput()
        self.mem_wb_register.writeOutput()
        self.muxMemtoReg.writeOutput()
        self.registerFile.writeOutput()


        self.brake.writeOutput()
        if self.brake.full_stop.value == 1:
            raise Break("Break instruction encountered")


        function = self.if_id_register.function_out.value
        is_signed = (function == 0b1000001 or function == 0b100011)
        if not is_signed and self.alu.overflow.value == 1:
            raise Overflow("overflow detected")
        
        
        
