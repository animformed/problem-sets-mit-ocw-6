# Similar to prior, but using lists instead of dictionaries for sums
import sys
filename = sys.argv[1]          # get the cmd argument after the filename and so on
numcols = int(sys.argv[2])
totals = [0] * numcols

for line in open(filename):
    cols = line.split(',')
    nums = [int(col) for col in cols]
    totals = [(x + y) for (x, y) in zip(nums, totals)]

print totals