from maya import cmds
#path: Folder luu tam
path = "C:/Users/Dell/OneDrive/Documents/maya/projects/default/scenes"
#selectOBJ = cmds.ls(sl=1)
#fileName = selectOBJ
# TempObject: Ten doi tuong
totalPathName = path + "/" + "TempObject"
#count = 1
#for i in fileName:
#    extension = ".obj"
#    if count == 1:
#        totalPathName = path+"/"+i
#        count += 1
#    elif count == int(len(fileName)):
#        totalPathName = totalPathName+"_"+i+extension
#    else:
#        totalPathName = totalPathName+"_"+i
#        count += 1
cmds.file(totalPathName, f=True, op="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1", typ="OBJexport", pr=True, es=True)