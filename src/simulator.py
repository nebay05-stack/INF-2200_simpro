'''
Code written for inf-2200, University of Tromso
'''

import sys
from mipsSimulator import MIPSSimulator, Break



def runSimulator(sim: MIPSSimulator):
    try:
        while True:
            sim.tick()
    except Break:
        print("\n--- Programmet er ferdig (Break nådd) ---")
        sim.printRegisterFile()
        sim.printDataMemory()

if __name__ == '__main__':
    assert len(sys.argv) == 2, f"Usage: python {sys.argv[0]} memoryFile"
    memoryFile = sys.argv[1]
    
    simulator = MIPSSimulator(memoryFile)
    runSimulator(simulator)
