# Sum columns in a text file separated by commas
filename = 'spam.txt'
sums = {}

for line in open(filename):
    print 'line ', line
    cols = line.split(',')
    print 'cols ', cols
    nums = [int(col) for col in cols]
    print 'num ', nums
    for(ix, num) in enumerate(nums):
        print (ix, num)
        sums[ix] = sums.get(ix, 0) + num
        print sums[ix]

for key in sorted(sums):
    print key, '=', sums[key]