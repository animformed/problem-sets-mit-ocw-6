import math, random, pylab

class Location(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def move(self, xc, yc):
        return Location(self.x + float(xc), self.y + float(yc))
    def getCoords(self):
        return self.x, self.y
    def getDist(self, other):
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2 + yDist**2)

class CompassPt(object):
    possibles = ('N', 'S', 'E', 'W')        # not self, since no copy for a new instance
    def __init__(self, pt):
        if pt in self.possibles:
            self.pt = pt
        else:
            raise ValueError('in CompassPt.__init__')
    def move(self, dist):
        if self.pt == 'N':
            return (0, dist)        # in x, y coord form
        elif self.pt == 'S':
            return (0, -dist)
        elif self.pt == 'E':
            return (dist, 0)
        elif self.pt == 'W':
            return (-dist, 0)
        else:
            raise ValueError('in CompassPt.move')

class Field(object):
    def __init__(self, drunk, loc):
        self.drunk = drunk          # drunk object
        self.loc = loc              # current location
    def move(self, cp, dist):
        oldLoc = self.loc
        xc, yc = cp.move(dist)      # move from CompassPt
        self.loc = oldLoc.move(xc, yc)      # move from Location
    def getLoc(self):
        return self.loc
    def getDrunk(self):
        return self.drunk

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def move(self, field, cp, dist = 1):
        if field.getDrunk() != self:        # to check if a drunk object exists, in field
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(dist):
            field.move(cp, 1) 

class UsualDrunk(Drunk):
    def move(self, field, dist = 1):
        cp = random.choice(CompassPt.possibles)
        Drunk.move(self, field, CompassPt(cp), dist)    # Note call to Drunk.move
        
class ColdDrunk(Drunk):
    def move(self, field, dist = 1):
        cp = random.choice(CompassPt.possibles)
        if cp == 'S':
            Drunk.move(self, field, CompassPt(cp), 2*dist)      # biased towards moving south twice as fast
        else:
            Drunk.move(self, field, CompassPt(cp), dist)

class EWDrunk(Drunk):
    def move(self, field, time = 1):
        cp = random.choice(CompassPt.possibles)
        while cp != 'E' and cp != 'W':
            cp = random.choice(CompassPt.possibles)
        Drunk.move(self, field, CompassPt(cp), time)
        
def performTrial(time, f):      # pass in the f field object
    start = f.getLoc()
    distances = [0.0]
    locs = []
    for t in range(1, time + 1):
        f.getDrunk().move(f)
        newLoc = f.getLoc()
        distance = newLoc.getDist(start)
        distances.append(distance)
        locs.append(newLoc)
    return distances, locs

def performSim(time, numTrials, drunkType):    
    distLists = []
    locLists = []
    for trial in range(numTrials):
        dr = drunkType('Drunk' + str(trial))
        f = Field(dr, Location(0, 0))
        distances, locs = performTrial(time, f)
        distLists.append(distances) 
        locLists.append(locs)
    return distLists, locLists

def ansQuest1(maxTime, numTrials, drunkType, title):
    means = []
    distLists = performSim(maxTime, numTrials, drunkType)
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distLists))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('avg. distance')
    pylab.xlabel('steps')
    pylab.title(title)
 
def ansQuest2(maxTime, numTrials, drunkType, title):  
    distLists, locLists = performSim(maxTime, numTrials, drunkType)
    means = []
    
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distLists))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title(title + ' Avg. Distance')
    
    lastX = []
    lastY = []
    for locList in locLists:
        x, y = locList[-1].getCoords()
        lastX.append(x)
        lastY.append(y)
    pylab.figure()
    pylab.scatter(lastX, lastY)
    pylab.xlabel('EW distance')    
    pylab.ylabel('NS distance')
    pylab.title(title + ' Final locations')
    
    pylab.figure()
    pylab.hist(lastX)
    pylab.xlabel('EW value')
    pylab.ylabel('Number of trials')
    pylab.title(title + ' Distribution of final EW Values')
    
numSteps = 500
numTrials = 400
i_title = 'UsualDrunk ' + str(numTrials) + ' Trials'
ansQuest2(numSteps, numTrials, UsualDrunk, i_title)
ansQuest2(500, 400, EWDrunk, 'EWDrunk')
pylab.show()
  
    
#numSteps = 500
#numTrials = 100
#ansQuest(numSteps, numTrials, UsualDrunk, 'UsualDrunk ' + str(numTrials) + ' Trials')
#ansQuest(numSteps, numTrials, ColdDrunk, 'ColdDrunk ' + str(numTrials) + ' Trials')
#ansQuest(numSteps, numTrials, EWDrunk, 'EWDrunk ' + str(numTrials) + ' Trials')
#pylab.show()