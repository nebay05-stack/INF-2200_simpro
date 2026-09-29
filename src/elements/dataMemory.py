'''
Implements CPU element for Data Memory in MEM stage.

Code written for inf-2200, University of Tromso
'''

from elements.memory import Memory
from common import Value
from typing import List
from elements.controll_unit import Controller

class DataMemory(Memory):
    def __init__(self, filename: str):
        Memory.__init__(self, filename)
        self.address: Value = Value(0)
        self.writedata: Value = Value(0)
        self.MemRead: Value = Value(0)
        self.MemWrite: Value = Value(0)
        
    def connectInputs(self, inputs: List[Value]):
        self.address = inputs[0]
        self.writedata = inputs[1]
        self.MemRead = inputs[2]
        self.MemWrite = inputs[3]

        raise AssertionError("connect not implemented in class DataMemory!")
    
    def writeOutput(self):
        # Remove this and replace with your implementation!
        controller = Controller()
        if controller.MemRead.value == 1:
            self.readdata = self.memory[self.address]


        
        raise AssertionError("writeOutput not implemented in class DataMemory!")
