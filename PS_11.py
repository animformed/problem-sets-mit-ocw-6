# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

from PS_11_Gui import *
import math, random, pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = {}
        for i in xrange(width):
            for j in xrange(height):
                self.tiles[(i, j)] = False
                
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        curr_pos = int(math.floor(pos.getX())), int(math.floor(pos.getY()))
        #print 'curr_pos', curr_pos
        self.tiles[curr_pos] = True
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m, n)]
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return len(self.tiles)
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return sum(self.tiles.values())
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        newX = random.random() * self.width
        newY = random.random() * self.height
        return newX, newY
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        check_pos = int(math.floor(pos.getX())), int(math.floor(pos.getY()))
        if check_pos in self.tiles:
            return True
        else:
            return False


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.d = random.randint(0, 359)     # get a random angle of direction
        self.room = room
        pos = self.room.getRandomPosition()      # get a random room position
        #print pos
        self.p = Position(*pos)              # return the room position to create a Position
        self.speed = speed
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.p
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.d
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.p = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.d = direction
        
class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
#        check if movement in this step collides with a wall:
#            if not:
#                move to a next tile in the current direction
#                set tile clean
#            else:
#                get a new random direction
#                continue all over
        
        check = True
        while check:
            check = False
            newPos = self.p.getNewPosition(self.d, self.speed)
            if self.room.isPositionInRoom(newPos):
                self.p = newPos
                self.room.cleanTileAtPosition(newPos)
            else:
                self.d = random.randint(0, 359)
                check = True

# === Problem 3

def performTrial(num_robots, speed, width, height, min_coverage, robot_type, visualize):
    
    cleanSteps = []
    rm = RectangularRoom(width, height)
    robots = []
    for i in xrange(num_robots):
        rb = robot_type(rm, speed)
        robots.append(rb)
    total_tiles = rm.getNumTiles()
    min_coverage = total_tiles * min_coverage
    if visualize:
        anim = RobotVisualization(num_robots, width, height)
    while rm.getNumCleanedTiles() < min_coverage:
        for robot in robots:
            robot.updatePositionAndClean()
        clean_p = int(round((rm.getNumCleanedTiles()/float(total_tiles))*100))
        cleanSteps.append(clean_p)
        if visualize:
            anim.update(rm, robots)
    if visualize:
        anim.done()
    return cleanSteps
        
    
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize=False):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    all_steps = []
    for i in xrange(num_trials):
        cSteps = performTrial(num_robots, speed, width, height, min_coverage, robot_type, visualize)
        all_steps.append(cSteps)
    return all_steps
            
# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    times = []
    pylab.figure()
    sizes = pylab.array(range(5, 30, 5))
    for size in sizes:
        c_res = runSimulation(num_robots=1, speed=1, width=size, height=size, min_coverage=0.75, num_trials=5, robot_type=Robot, visualize=False)
        c_means = computeMeans(c_res)
        times.append(len(c_means))
    #print times
    pylab.plot(sizes*sizes, times)
    pylab.title('Average cleaning timesteps by ' + str(1) + ' Robot(s) of variable room sizes' + '\nwith min coverage of ' + str(int(0.75*100)) + ' %, in ' + str(5) + ' trial(s)')
    pylab.ylabel('Average Time Steps')
    pylab.xlabel('Room Area')
    #pylab.legend(sizes,title='Room sizes', loc = 'best')

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    times = []
    pylab.figure()
    for i in xrange(1, 11):
        c_res = runSimulation(num_robots=i, speed=1, width=25, height=25, min_coverage=0.75, num_trials=10, robot_type=Robot, visualize=False)
        c_times = computeMeans(c_res)
        times.append(len(c_times))
    pylab.plot(range(1,11), times)
    pylab.title('Mean cleaning timesteps by ' + str(10) + ' Robot(s) of Room size 25X25' + '\nwith min coverage of ' + str(int(0.75*100)) + ' %, in ' + str(10) + ' trial(s)')
    pylab.xlabel('Number of Robot(s)')
    pylab.ylabel('Mean cleaning timesteps')
    
def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    times = []
    pylab.figure()
    sizes = ((20, 20), (25, 16), (40, 10), (50, 8), (80, 5), (100, 4))
    size_ratio = []
    for m, n in sizes:
        c_res = runSimulation(num_robots=2, speed=1, width=m, height=n, min_coverage=0.75, num_trials=5, robot_type=Robot, visualize=False)
        c_times = computeMeans(c_res)
        times.append(len(c_times))
        size_ratio.append((float(m)/float(n)))
    #print times, size_ratio
    pylab.plot(size_ratio, times)
    pylab.title('Mean cleaning timesteps by ' + str(2) + ' Robot(s) of variable room sizes' + '\nwith min coverage of ' + str(int(0.75*100)) + ' %, in ' + str(5) + ' trial(s)')
    pylab.xlabel('Room size ratio')
    pylab.ylabel('Mean cleaning timesteps')
    #pylab.legend(size_ratio,title='Room size ratio', loc = 'best')
        

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
#    mean time vs coverage in each curve for robots varying from 1 to 5
    times = []
    pylab.figure()
    min_coverages = range(25,125,25)
    for min_cover in min_coverages:
        sub_times = []
        for robots in range(1,6):
            c_res = runSimulation(num_robots=robots, speed=1, width=25, height=25, min_coverage=min_cover*0.01, num_trials=5, robot_type=Robot, visualize=False)
            c_times = computeMeans(c_res)
            sub_times.append(len(c_times))
        times.append(sub_times)
    print times
    pylab.plot(min_coverages, times)
    pylab.title('Mean cleaning timesteps by 1 to 5 Robot(s) of room size 25X25' + '\nwith increasing min coverages, in ' + str(5) + ' trial(s)')
    pylab.xlabel('Min. % coverage area')
    pylab.ylabel('Mean cleaning timesteps decreases as robots increase')
    pylab.legend(min_coverages,title='Min % Coverage', loc = 'best')
    
        


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        check = True
        while check:
            check = False
            self.d = random.randint(0, 359)
            newPos = self.p.getNewPosition(self.d, self.speed)
            if self.room.isPositionInRoom(newPos):
                self.p = newPos
                self.room.cleanTileAtPosition(newPos)
            else:
                self.d = random.randint(0, 359)
                check = True    


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here

if __name__ == '__main__':
#    res = runSimulation(5, 1, 20, 20, 1, 10, Robot, visualize=False)
#    print res
    res = runSimulation(5, 1, 20, 20, 1, 10, RandomWalkRobot, visualize= True)
    print res
#    showPlot1()
#    showPlot2()
#    showPlot3()
#    showPlot4()
#    pylab.show()
    