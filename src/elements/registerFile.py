'''
Code written for inf-2200, University of Tromso
'''

from elements.cpuElement import CPUElement
import common
from typing import List
from common import Value

class RegisterFile(CPUElement):
    def __init__(self):
        # Dictionary mapping register number to register value
        self.register = {}
        # Note that we won't actually use all the registers listed here...
        self.registerNames = ['$zero', '$at', '$v0', '$v1', '$a0', '$a1', '$a2', '$a3',
                              '$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7',
                              '$s0', '$s1', '$s2', '$s3', '$s4', '$s5', '$s6', '$s7',
                              '$t8', '$t9', '$k0', '$k1', '$gp', '$sp', '$fp', '$ra']
        # All registers default to 0
        for i in range(0, 32):
            self.register[i] = 0

        # Inputs 
        self.readregister_1: Value = Value(0)
        self.readregister_2: Value = Value(0)
        self.writeregister: Value = Value(0)
        self.writedata: Value = Value(0)
        self.reg_write: Value = Value(0) 

        # Outputs 
        self.readdata_1 = Value(0)
        self.readdata_2 = Value(0)

    def connectInputs(self, inputs: List[Value]):
        self.readregister_1 = inputs[0]
        self.readregister_2 = inputs[1]
        self.writeregister = inputs[2]
        self.writedata = inputs[3]
        self.reg_write = inputs[4]

    def writeOutput(self):
        assert isinstance(self.readregister_1.value, int) and isinstance(self.readregister_2.value, int)
        
        self.readdata_1.value = self.register.get(self.readregister_1.value, 0)
        self.readdata_2.value = self.register.get(self.readregister_2.value, 0)

        if self.reg_write.value == 1:
            reg_dest = self.writeregister.value
            data_to_write = self.writedata.value
        
            if reg_dest != 0: 
                self.register[reg_dest] = data_to_write & 0xFFFFFFFF
        

        


    def printAll(self):
        '''
        Print the name and value in each register.
        '''

        print()
        print("Register file")
        print("================")
        for i in range(0, 32):
            print(f"{self.registerNames[i]} \t=> {common.fromUnsignedWordToSignedWord(self.register[i])} ({hex(int(self.register[i]))[:-1]})")
        print("================")
        print()
        print()
