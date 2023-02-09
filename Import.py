from maya import cmds

path = "C:/Users/Dell/OneDrive/Documents/maya/projects/default/scenes"
totalPathName = path + "/" + "TempObject.obj"
cmds.file(totalPathName, type="OBJ", iv=True, i=True, mnc=False, ns="TempObject", op="mo=1", ifr=True, itr="override")