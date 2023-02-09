from maya import cmds

path = "C:/Users/Dell/OneDrive/Documents/maya/projects/default/scenes"
totalPathName = path + "/" + "TempObject.obj"
temp = cmds.file(totalPathName, type="OBJ", i=True, rdn=True, mbl=True, mnc=True, rpr=":", op="mo=0", ifr=True, itr="combine")
