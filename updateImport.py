from maya import cmds

path = "C:/Users/Dell/OneDrive/Documents/maya/projects/default/scenes"
totalPathName = path + "/" + "TempObject.obj"
pylysur = "polySurface1"
selected = cmds.ls(sl=True, long=True) or []
for eachSel in selected:
    changeObj = eachSel
cmds.delete(changeObj, constructionHistory = True)
cmds.file(totalPathName, type="OBJ", i=True, rdn=True, mbl=True, mnc=True, rpr=":", op="mo=0", ifr=True, itr="combine")
cmds.select(pylysur, r=True)
cmds.select(changeObj, tgl=True)
cmds.blendShape(pylysur, changeObj)
#cmds.blendShape("blendShape1", edit =True, en=1.0)
cmds.blendShape("blendShape1", edit =True, w=(0, 1.0))
cmds.delete(pylysur)
