# Comments regarding module
#
#

## Imports
from sb3objects import sb3block
from sb3helper.sb3helper import *
import copy

## Globals

variableDict = {} # stored as dict idx : [name, targetName, value] | variable handled as global (targetname = None) if cant find in local
listDict = {} # stored as dict idx : [name, targetName, [listvalues] ] | variable handled as global (targetname = None) if cant find in local
broadcastDict = {} # stored as dict idx : [name, targetName]  | broadcast handled as global (targetname = None) if cant find in local

def getVariableDict(): return variableDict
def getListDict(): return listDict
def getBroadcastDict(): return broadcastDict

def getVariableArr_byId(idx):
        for key in getVariableDict():
            if key == idx:
                return getVariableDict()[key]
        return None

def containsVariable_byId(idx):
    for key in getVariableDict():
        if key == idx:
            return True
    return False

def getBroadcastArr_byId(idx):
        for key in getBroadcastDict():
            if key == idx:
                return getBroadcastDict()[key]
        return None

def containsBroadcast_byId(idx):
    for key in getBroadcastDict():
        if key == idx:
            return True
    return False

## Define

## Helper functions

## Class declaration

class SB3Target:       
    def __init__(self, targetJsonObj):
        self.isStage = targetJsonObj['isStage']
        self.type = "stage" if targetJsonObj['isStage'] else "sprite"
        self.name = targetJsonObj['name']
        
        self.targetBlockList = []

        # extract block and add to list
        for blockIdx in targetJsonObj['blocks']:
            self.targetBlockList.append(sb3block.SB3Block(self.name, blockIdx, targetJsonObj['blocks'][blockIdx]))
        
        # extract variable and add to list
        for idx in targetJsonObj['variables']:
            variableDict[idx] = [targetJsonObj['variables'][idx], None, None] # all as global
        
        # extract list and add to list
        for idx in targetJsonObj['lists']:
            listDict[idx] = [targetJsonObj['lists'][idx], None, []] # all as global

        # extract broadcast and add to list
        for idx in targetJsonObj['broadcasts']:
            broadcastDict[idx] = [targetJsonObj['broadcasts'][idx], None] # all as global

    # Class Methods
    def get_self(self):
        return self

    def get_isStage(self):
        return self.isStage

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_blockList(self):
        return self.targetBlockList
    
    def getBlock_byId(self, idx):
        for tmpBlockObj in self.get_blockList():
            if tmpBlockObj.get_idx() == idx:
                return tmpBlockObj
        return None

    def containsBlock_byId(self, idx):
        for tmpBlockObj in self.get_blockList():
            if tmpBlockObj.get_idx() == idx:
                return True
        return False
    
    def traversalEngin_print(self):
        print("# " + str(self.get_name()))
        print("# -----")
        for indivBlock in self.get_blockList():
            if indivBlock.get_topLevel() == True:
                indent = 0
                self.unpack(indent, [0, indivBlock.get_idx()])
                print()
                print()

    def unpack(self, indent, arr_type_val):
        if arr_type_val[0] == 0: # indicate is a block
            if self.containsBlock_byId(arr_type_val[1]): # is a block
                currBlock = self.getBlock_byId(arr_type_val[1])

                #currOpcode = currBlock.get_opcode()
                self.decodeBlockPrint(indent, currBlock)
                #printInd(indent,currOpcode)

                if(currBlock.get_next() != None):
                    print()
                    self.unpack(indent, [0,currBlock.get_next()])
        else: # indicate not a block
            if(3 < arr_type_val[0] < 11): #primitive
                return arr_type_val[1]
            elif(arr_type_val[0] == 11): #broadcast
                if(containsBroadcast_byId(arr_type_val[1])):
                    broadcastValArr = getBroadcastArr_byId(arr_type_val[1])
                    return str(broadcastValArr[0])
            elif(arr_type_val[0] == 12): #variable
                if(containsVariable_byId(arr_type_val[1])):
                    varValArr = getVariableArr_byId(arr_type_val[1])
                    return str(varValArr[0][0])
            elif(arr_type_val[0] == 13): #list
                # if(containsVariable_byId(arr_type_val[1])):
                #     varValArr = getVariableArr_byId(arr_type_val[1])
                #     return str(varValArr[0][0])
                return str(arr_type_val) + "_lst"
            else:
                return str(arr_type_val) + "_npt"
                #return ("notPrimitiveType")

    def decodeBlockPrint(self,indent,currBlock):
        prInd(indent,currBlock.get_opcode())
        currBlock.markReachable()
        if(len(currBlock.get_blockFieldDict()) != 0):

            blkFiDict = copy.deepcopy(currBlock.get_blockFieldDict())

            pr("[")
            fiCtr = 1
            for indivFinKey in blkFiDict:
                if fiCtr > 1 and fiCtr <= len(blkFiDict):
                    pr(", ")
                pr(blkFiDict[indivFinKey][0])
                fiCtr += 1
            pr("]")

            #pr("[" + str(currBlock.get_blockFieldDict()) + "]")
            #pr("(field " + str(currBlock.get_blockFieldDict()) + ")")
            #pr("[" + unpack() + "]")
            #to unpack
        if(len(currBlock.get_blockInputDict()) != 0):
            
            blkInDict = copy.deepcopy(currBlock.get_blockInputDict())

            substack1 = None
            substack2 = None
            operand1 = None
            operand2 = None

            if "SUBSTACK" in blkInDict:
                substack1 = blkInDict["SUBSTACK"]
                del blkInDict["SUBSTACK"]
            if "SUBSTACK2" in blkInDict:
                substack2 = blkInDict["SUBSTACK2"]
                del blkInDict["SUBSTACK2"]

            if "OPERAND1" in blkInDict:
                operand1 = blkInDict["OPERAND1"]
                del blkInDict["OPERAND1"]
            if "OPERAND2" in blkInDict:
                operand2 = blkInDict["OPERAND2"]
                del blkInDict["OPERAND2"]
            
            if(operand1):
                pr("(")
                #pr("/op1 : ")
                if operand1[0] == 0:
                    self.unpack(0,operand1)
                else:
                    pr(self.unpack(0, operand1))

                if(operand2): # assuming if theres an operand 2 only if theres an operand 1
                    pr(", ")
                    if operand2[0] == 0:
                        self.unpack(0,operand2)
                    else:
                        pr(self.unpack(0, operand2))
                pr(")")

            if len(blkInDict) != 0:
                #pr("("+ str(blkInDict) + "   |   ")
                pr("(")
                inCtr = 1
                for indivInKey in blkInDict:
                    if inCtr > 1 and inCtr <= len(blkInDict):
                        pr(", ")
                    #pr("(input_" + str(indivInKey) + " : " + str(currBlock.get_blockInputDict()[indivInKey]) + ")")
                    #switch whether just print value or need to decode
                    
                    if(blkInDict[indivInKey][0] == 0): # isBlock
                        self.unpack(0, blkInDict[indivInKey])
                    elif(3 < blkInDict[indivInKey][0] < 11): # isValue
                        pr(self.unpack(0, blkInDict[indivInKey]))
                    elif(blkInDict[indivInKey][0] == 11): # isBroadcast
                        pr(self.unpack(0,blkInDict[indivInKey]))
                    else:
                        pr("HANDLE THE REST_aabbcc")
                    inCtr += 1
                pr(")")
            
            if(substack1):
                pr("{\n")
                self.unpack(indent + 1, substack1)
                print()
                prInd(indent,"}")
            if(substack2):
                pr("{\n")
                self.unpack(indent + 1, substack2)
                print()
                prInd(indent,"}")


        