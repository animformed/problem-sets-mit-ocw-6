# Find the largest Python source file on the module import search path
import os, pprint, sys
visited = {}
allsizes = []
for srcpath in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcpath):
        thisDir = os.path.normpath(thisDir)
        if thisDir.upper() in visited:
            continue
        else:
            visited[thisDir.upper()] = True
        for filename in filesHere:
            if filename.endswith('.py'):
                fullname = os.path.join(thisDir, filename)
                filesize = os.path.getsize(fullname)
                allsizes.append((filesize, fullname))
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
           
        