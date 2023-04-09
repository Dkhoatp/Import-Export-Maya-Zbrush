import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import os
from maya import cmds

dirName = "C:/tempObject"
path = "C:/tempObject"
class addIEButton(OpenMayaMPx.MPxCommand):

    def doIt(self, argList):
        self.CallMenu()

    def CallMenu(self):
        # Create directory 
        try:
            # Create target Directory
            os.mkdir(dirName)
        except FileExistsError:
            pass
        createMainMenu()

def createMainMenu():
    cmds.menu(label=u"IEport", tearOff=False, p="MayaWindow")
    cmds.menuItem(l=u"Import", c=importFunc)
    cmds.menuItem(l=u"Export", c=exportFunc)
    cmds.menuItem(d=True)
    cmds.menuItem(l=u"Update", c=updateFunc)
    cmds.menuItem(d=True)
    cmds.menuItem(l=u"delete History", c=delHistory)

def importFunc(self):
    totalPathName = path + "/" + "TempObject.obj"
    temp = cmds.file(totalPathName, type="OBJ", i=True, rdn=True, mbl=True, mnc=True, rpr=":", op="mo=0", ifr=True, itr="combine")

def exportFunc(self):
    totalPathName = path + "/" + "TempObject"
    cmds.file(totalPathName, f=True, op="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1", typ="OBJexport", pr=True, es=True)


def updateFunc(self):
    totalPathName = path + "/" + "TempObject.obj"
    OriginObject = cmds.ls(selection=True)[0]
    selected = cmds.ls(sl=True, long=True) or []
    for eachSel in selected:
        changeObj = eachSel
    cmds.file(totalPathName, type="OBJ", i=True, rdn=True, mbl=True, mnc=True, rpr=":", op="mo=0", ifr=True, itr="combine")
    cmds.select(OriginObject, r=True)
    cmds.select(changeObj, tgl=True)
    cmds.blendShape(OriginObject, changeObj)
    # cmds.blendShape("blendShape1", edit =True, en=1.0)
    cmds.blendShape("blendShape1", edit=True, w=(0, 1.0))
    cmds.delete(changeObj)
    
def delHistory(self):
    os.remove("C:/tempObject/TempObject.obj")
    os.remove("C:/tempObject/TempObject.mtl")
def creator():
    return OpenMayaMPx.asMPxPtr(addIEButton())


def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj, "nowhere", "1.0", "Any")
    try:
        plugin.registerCommand("addIEButton", creator)
    except:
        raise RuntimeError("Failed to register command")


def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    try:
        plugin.deregisterCommand("addIEButton")
    except:
        raise RuntimeError("Failed to unregister command")
