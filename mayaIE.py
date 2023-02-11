import os
from maya import cmds
# Create directory
dirName = "C:/tempObject"
path = "C:/tempObject"
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName,  "Created")
except FileExistsError:
    pass

def createMainMenu():
    cmds.menu(label=u"IEport", tearOff=False, p="MayaWindow")
    cmds.menuItem(l=u"Import", c=importFunc)
    cmds.menuItem(l=u"Export", c=exportFunc)
    cmds.menuItem(d=True)
    cmds.menuItem(l=u"Update", c=updateFunc)

def importFunc(self):
    totalPathName = path + "/" + "TempObject.obj"
    temp = cmds.file(totalPathName, type="OBJ", i=True, rdn=True, mbl=True, mnc=True, rpr=":", op="mo=0", ifr=True, itr="combine")

def exportFunc(self):
    totalPathName = path + "/" + "TempObject"
    cmds.file(totalPathName, f=True, op="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1", typ="OBJexport", pr=True, es=True)


def updateFunc(self):
    totalPathName = path + "/" + "TempObject.obj"
    pylysur = "polySurface1"
    selected = cmds.ls(sl=True, long=True) or []
    for eachSel in selected:
        changeObj = eachSel
    cmds.delete(changeObj, constructionHistory=True)
    cmds.file(totalPathName, type="OBJ", i=True, rdn=True, mbl=True, mnc=True, rpr=":", op="mo=0", ifr=True, itr="combine")
    cmds.select(pylysur, r=True)
    cmds.select(changeObj, tgl=True)
    cmds.blendShape(pylysur, changeObj)
    # cmds.blendShape("blendShape1", edit =True, en=1.0)
    cmds.blendShape("blendShape1", edit=True, w=(0, 1.0))
    cmds.delete(pylysur)

createMainMenu()
