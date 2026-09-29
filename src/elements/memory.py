'''
Implements base class for memory elements.

Note that since both DataMemory and InstructionMemory are subclasses of the Memory
class, they will read the same memory file containing both instructions and data
memory initially, but the two memory elements are treated separately, each with its
own, isolated copy of the data from the memory file.

Code written for inf-2200, University of Tromso
'''

from elements.cpuElement import CPUElement
import common

class Memory(CPUElement):
    def __init__(self, filename: str):
    
        # Dictionary mapping memory addresses to data
        self.memory = {}
        
        self.initializeMemory(filename)
    
    def initializeMemory(self, filename: str):
        with open(filename, 'r') as f:

         for line in f:
             line = line.strip()

             if not line or line.startswith('#'):
                continue

             adress_value = line.split()

             if len(adress_value) >= 2:
                adress = int(adress_value[0], 0)
                value = int(adress_value[1], 0)

                self.memory[adress] = value

        raise AssertionError("initializeMemory not implemented in class Memory!")
        
    def printAll(self):
        for key in sorted(self.memory.keys()):
            print(f"{hex(int(key))}\t=> {common.fromUnsignedWordToSignedWord(self.memory[key])}\t({hex(int(self.memory[key]))})")
