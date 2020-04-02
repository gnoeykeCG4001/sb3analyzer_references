#### Comments regarding module

### Imports
import json
from sb3objects import sb3target
from sb3objects import sb3block
from sb3analyzer import sb3analyzer

### Class Methods

def analyzeProj(Proj):
    analyzeObj = sb3analyzer.SB3Analyzer(Proj)

    analyzeObj.getDeadCode_BlockList()



class SB3Project:

    def __init__(self, rawProjString):
        projectJsonObj = json.loads(rawProjString)
        sectionHeaderList = list(projectJsonObj) # ['targets', 'monitors', 'extensions', 'meta']

        self.targetsList = []

        for indivSectionTitle in sectionHeaderList:
            # Create targets
            if (indivSectionTitle == "targets"):
                for targetNum in range(len(projectJsonObj[indivSectionTitle])):
                    #tmpTargetName = projectJsonObj[indivSectionTitle][targetNum]['name']
                    tmpTargetObj = sb3target.SB3Target(projectJsonObj[indivSectionTitle][targetNum])
                    self.targetsList.append(tmpTargetObj)

            # Create monitors
            if (indivSectionTitle == "monitors"):
                pass

            # Create extensions
            if (indivSectionTitle == "extensions"):
                pass

            # Create meta
            if (indivSectionTitle == "meta"):
                pass

    def printProj(self):

        print("Global Variables : " + str(sb3target.getVariableDict()))
        print("Global Lists : " + str(sb3target.getListDict()))
        print("Global Broadcasts : " + str(sb3target.getBroadcastDict()))
        print()

        for indivTargetIdx in range(len(self.targetsList)):
            #print(self.targetsList[indivTargetIdx].get_self().get_name())
            #print("-----")            

            self.targetsList[indivTargetIdx].get_self().traversalEngin_print()
            print()

        #print(sectionHeaderList)
    
    def getTargetList(self):
        return self.targetsList