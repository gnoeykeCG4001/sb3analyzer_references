# Comments regarding module
#
#

## Imports
from sb3objects import sb3block_inputNfield

## Globals

## Define

## Helper functions

## Class declaration

'''
"opcode": "control_repeat_until",
"next": null,
"parent": "+8Wtq6[reo9n/);{VC5o",
"inputs": 
"fields": {},
"shadow": false,
"topLevel": false
x
y
'''

class SB3Block:

    # Constructor
        
    def __init__(self, containerTarget, blockIdx, blockJsonObj):
        
        self.containerTarget = containerTarget
        self.idx = blockIdx
        self.opcode = blockJsonObj['opcode']
        #self.opcodeType = 
        self.next = blockJsonObj['next']
        self.parent = blockJsonObj['parent']
        self.topLevel = blockJsonObj['topLevel']
        self.blockInputDict = {}
        self.blockFieldDict = {}

        self.reachable = False
        
        # check if is target attribute getter (size/direction etc)

        # extract inputs and add to list

        inputLabel = list(blockJsonObj['inputs'])
        for indivInputLabel in inputLabel:
            # Label : [Type, Value]
            # blockJsonObj['inputs'][indivInputLabel][0] is discarded
            self.blockInputDict[indivInputLabel] = sb3block_inputNfield.decodeInput(blockJsonObj['inputs'][indivInputLabel][1])

        # extract fields and add to list
        
        fieldLabel = list(blockJsonObj['fields'])
        for indivFieldLabel in fieldLabel:
            # Label : [NameId, Reference]
            self.blockFieldDict[indivFieldLabel] = sb3block_inputNfield.decodeField(blockJsonObj['fields'][indivFieldLabel])

    # Class Methods
    def get_self(self):
        return self
    
    def get_idx(self):
        return self.idx

    def get_opcode(self):
        return self.opcode

    def get_next(self):
        return self.next

    def get_parent(self):
        return self.parent
    
    def get_topLevel(self):
        return self.topLevel

    def get_blockInputDict(self):
        return self.blockInputDict

    def get_blockFieldDict(self):
        return self.blockFieldDict

    def markReachable(self):
        self.reachable = True
    
    def isReachable(self):
        return self.reachable