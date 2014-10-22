import math, random, pylab


class Location(object):
    """
    Manages the current location of the subject.
    """
    def __init__(self, x, y):
        """
        Takes in the new coords values for x and y for the constructor, while creating 
        a new instance for a new location.
        """
        self.x = float(x)
        self.y = float(y)
    def move(self, xc, yc):
        """
        Move the current location in x and y by new amounts. Returns a new Location 
        object with the new updated location.
        """
        return Location(self.x + float(xc), self.y + float(yc))
    def getCoords(self):
        """
        Returns the x and y coords for the current location for the Location object.
        """
        return self.x, self.y
    def getDist(self, other):
        """
        Returns the displacement of a Location from another Location in float.
        """
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2 + yDist**2)       # hypotenuse

class CompassPt(object):
    """
    Creates and manages the compass direction for movements.
    """
    possibles = ('N', 'S', 'E', 'W')        # not self, since no copy for a new instance
    def __init__(self, pt):
        """
        Creates a compass direction variable for the instance(object), based on a correct input.
        """
        if pt in self.possibles:
            self.pt = pt
        else:
            raise ValueError('in CompassPt.__init__')
    def move(self, dist):
        """
        Sets and returns the direction of movement in x, y form based on the compass direction variable 
        in the instance. The movement can proceed in only one axis.
        """
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
    """
    Container class for managing Location and Drunk objects. 
    """
    def __init__(self, drunk, loc):
        """
        For each instance object, it accepts a Drunk and a Location object as attributes.
        """
        self.drunk = drunk          # drunk object
        self.loc = loc              # current location
    def move(self, cp, dist):
        """
        oldLoc = Location based on the Location object in the instance
        
        xc, yc = Getting the direction of movement based on the passed in CompassPt object
        
        It also updates the current Location object as attribute with a new Location object after a
        movement based on the compass direction.
        """
        oldLoc = self.loc
        xc, yc = cp.move(dist)      # move from CompassPt
        self.loc = oldLoc.move(xc, yc)      # move from Location
    def getLoc(self):
        """
        Returns the Location object stored as an attribute, from the instance.
        """
        return self.loc
    def getDrunk(self):
        """
        Returns the Drunk object stored as an attribute, from the instance.
        """
        return self.drunk
    
class Drunk(object):
    """
    Manages a Drunk object. Only one drunk object exists in a session.
    """
    def __init__(self, name):
        """
        Accepts a name attribute for the Drunk object.
        """
        self.name = name
    def move(self, field, time = 1):
        """
        Accepts a field object, and number of times for a movement. Default is 1.
        
        First check to see if a Drunk object has been created and passed in the Field
        object. From the Field, the getDrunk() returns the reference for the Drunk object,
        if it exists.
        """
        if field.getDrunk() != self:        # to check if a drunk object exists, in field
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            field.move(pt, 1)

def performTrial(time, f):      # pass in the f field object
    start = f.getLoc()
    distances = [0.0]
    for t in range(1, time + 1):
        f.getDrunk().move(f)
        newLoc = f.getLoc()
        distance = newLoc.getDist(start)
        distances.append(distance)
    return distances

drunk = Drunk('Homer Simpson')
for i in range(3):
    f = Field(drunk, Location(0, 0))
    distances = performTrial(500, f)        # 500 steps on the field
    pylab.plot(distances)
pylab.title('Homer\'s Random Walk')
pylab.xlabel('Time')
pylab.ylabel('Distance from Origin')

pylab.show()
#assert False

#Takes the amount of time, no of steps for each trial, plus the number of trials
def performSim(time, sumTrials):    
    distLists = []
    for trial in range(sumTrials):
        dr = Drunk('Drunk' + str(trial))
        f = Field(dr, Location(0, 0))
        distances = performTrial(time, f)
        distLists.append(distances) 
    return distLists

def ansQuest(maxTime, numTrials):
    means = []
    distLists = performSim(maxTime, numTrials)
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distLists))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('Average Distance vs. Time (' + str(len(distLists)) + ' trials')
    
ansQuest(500, 200) # each trial be 500 steps, and run 100 trials
pylab.show()

   
        
        
        
    