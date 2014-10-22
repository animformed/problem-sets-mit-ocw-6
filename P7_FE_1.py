# Find the largest Python source file in a single directory
import os, glob
dirname = r'C:\Python26\Lib'      # \ cannot be used at the end because it wouldn't work with the quote.
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')   #translates to 'C:\\Python26\\Lib\\*.py'. os.sep provides \\
for filename in allpy:
    filesize = os.path.getsize(filename)        # get the size of the file
    allsizes.append((filesize, filename))       # append a tuple of the filename and filesize
    
allsizes.sort()
print allsizes[:2]          # print the first two smallest sizes
print allsizes[-2:]         # print the last two largest sizes
