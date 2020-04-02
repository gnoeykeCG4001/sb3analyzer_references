#### Comments regarding module

### Imports
import zipfile
#from sb3analyzer import sb3analyzer
from sb3objects import sb3project

### Globals
sb3fileName = "CatJumpJump.sb3"

### File Handling
sb3file = zipfile.ZipFile(sb3fileName, 'r')
projectJsonFile = sb3file.read('project.json')
projectJsonString = "".join(projectJsonFile.decode("ascii","ignore")) # protection from using unknown unicode characters

### Create Project Assets
Project = sb3project.SB3Project(projectJsonString)

### Do analysis
#Project.printProj()

sb3project.analyzeProj(Project)