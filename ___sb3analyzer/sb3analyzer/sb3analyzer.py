# Comments regarding module
#
#

## Imports
#from sb3objects import sb3block_inputNfield
import sys
sys.path.append('/__SB3Analyzer/sb3objects')
from sb3objects import sb3project

## Globals

## Define

## Helper functions

## Class declaration

class SB3Analyzer:

    # Constructor
    
    # score variables
    deadCode_BlockList = []

    def __init__(self, Proj):
        self.proj = Proj
        
        

    # Class Methods
    def get_self(self):
        return self

    def getDeadCode_BlockList(self):
        self.mark_print()
        tList = self.proj.getTargetList()

        for t in tList:
            for indivBlock in t.get_blockList():
                if not indivBlock.isReachable():
                    self.deadCode_BlockList.append([t.get_name(),indivBlock])
        
        print("\n\n\ndead blocks = " + str(len(self.deadCode_BlockList)))


    def mark_print(self):
        self.proj.printProj()
    
        