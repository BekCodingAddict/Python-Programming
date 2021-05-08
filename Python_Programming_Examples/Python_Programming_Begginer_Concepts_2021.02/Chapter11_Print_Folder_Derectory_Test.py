import os
for dirName,subDirList,fNames in os.walk("A:/"):
  for fname in fNames:
    print(os.path.join(dirName,fname))