import math, random, pylab

"""
Does a simulation where it flips a coin randomly with a given number of flips
"""
def flipTrial(numFlips):
    heads, tails = 0, 0                 
    for i in xrange(0, numFlips):     # like range() but generates an object instead of list, and is useful in loops. More memory efficient.
        coin = random.randint(0, 1)     # assign 0 or 1 to a head or tail randomly in a flip
        if coin == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails

def simFlips(numFlips, numTrials):      # performs and displays the simulation result
    diffs = []                          # diffs to know if there was a fair Trial. It has the absolute differences of heads and tails in each trial
    for i in xrange(0, numTrials):           
        heads, tails = flipTrial(numFlips)
        diffs.append(abs(heads - tails))
                
    diffs = pylab.array(diffs)          # create an array of diffs
    diffMean = sum(diffs)/len(diffs)    # average of absolute differences of heads and tails from each trial
    diffPercent = (diffs/float(numFlips)) * 100     # create an array of percentage of each diffs from its no. of flips.
    percentMean = sum(diffPercent)/len(diffPercent)     # create a percent mean of all diffPercents in the array
    
    pylab.hist(diffs)                   # displays the distribution of elements in diffs array
    pylab.axvline(diffMean, color = 'r', label = 'Mean')
    pylab.legend()
    titleString = str(numFlips) + ' Flips, ' + str(numTrials) + ' Trials'
    pylab.title(titleString)
    pylab.xlabel('Difference between heads and tails')
    pylab.ylabel('Number of Trials')
    
    pylab.figure()
    pylab.plot(diffPercent)
    pylab.axhline(percentMean, color = 'r', label = 'Mean')
    pylab.legend()
    pylab.title(titleString)
    pylab.xlabel('Trial Number')
    pylab.ylabel('Percent Difference between heads and tails')

simFlips(1000, 100)
pylab.show()   