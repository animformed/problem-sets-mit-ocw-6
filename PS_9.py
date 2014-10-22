# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        import math
        return math.pi*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        cond = False
        if type(other) == Triangle:
            if other.area() == self.area():
                cond = True
        return cond
#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any 
        needed variables
        """
        self.shapeSet = {'s':[],'c':[],'t':{'b':[],'h':[]}}
        ## TO DO
    def addShape(self):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        en_list = ['s', 'c', 't']
        inp = True
        while(inp):
            sh = raw_input('Add a Square(s), Circle(c) or a Triangle(t): ')
            if sh not in en_list:
                print 'Invalid input. Enter again.'
                continue
            inp = False
        while sh:
            if sh == 's':
                while True:
                    sh_side = raw_input('Enter the side of the square: ')
                    if float(sh_side) in self.shapeSet[sh]:
                        print 'Square exists. Enter a new side.'
                        continue
                    self.shapeSet[sh].append(float(sh_side))
                    break
            if sh == 'c':
                while True:
                    sh_radius = raw_input('Enter the radius of the circle: ')
                    if float(sh_radius) in self.shapeSet[sh]:
                        print 'Circle exists. Enter a new radius.'
                        continue
                    self.shapeSet[sh].append(float(sh_radius))
                    break
            if sh == 't':
                en = True
                while en:
                    en = False
                    sh_base = raw_input('Enter the base of the triangle: ')
                    sh_height = raw_input('Enter the height of the triangle: ')
                    base_it = self.shapeSet[sh]['b']
                    height_it = self.shapeSet[sh]['h']
                    for i in range(len(self.shapeSet[sh]['b'])):
                        if float(sh_base) == self.shapeSet[sh]['b'][i] and float(sh_height) == self.shapeSet[sh]['h'][i]:
                            print 'Triangle exists. Enter again.'
                            en = True
                self.shapeSet[sh]['b'].append(float(sh_base))
                self.shapeSet[sh]['h'].append(float(sh_height))

            break
        
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.iter_list = []
        self.ix = 0
        for i in range(len(self.shapeSet['c'])):
            sh = Circle(self.shapeSet['c'][i])
            self.iter_list.append(str(sh))
        for i in range(len(self.shapeSet['s'])):
            sh = Square(self.shapeSet['s'][i])
            self.iter_list.append(str(sh))
        for i in range(len(self.shapeSet['t']['h'])):
            sh = Triangle(self.shapeSet['t']['b'][i], self.shapeSet['t']['h'][i])
            self.iter_list.append(str(sh))
        return self
                
    def next(self):
        if self.ix == len(self.iter_list):
            raise StopIteration
        item = self.iter_list[self.ix]
        self.ix += 1
        return item
        
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        res_str = ''
        for item in self.shapeSet['c']:
            sh = Circle(item)
            res_str = res_str + str(sh) + '\n'
        for item in self.shapeSet['s']:
            sh = Square(item)
            res_str = res_str + str(sh) + '\n'
        for i in range(len(self.shapeSet['t']['h'])):
            sh = Triangle(self.shapeSet['t']['b'][i], self.shapeSet['t']['h'][i])
            res_str = res_str + str(sh) + '\n'
        if res_str == '':
            res_str += 'No input shapes in the set.'
        res_str = res_str.rstrip()
        return res_str
        ## TO DO
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    import math
    res = ()
    #shapes.shapeSet = {'s':[],'c':[],'t':{'b':[],'h':[]}}
    shapeDict = shapes.shapeSet
    
    l_s_area = 0
    if len(shapeDict['s']) > 0:
        for i in range(len(shapeDict['s'])):
            tmp_area = Square(shapeDict['s'][i]).area()
            if l_s_area < tmp_area:
                l_s_area = tmp_area
        #print l_s_area
        inp = round(math.sqrt(l_s_area), 1)
        res += (Square(inp),)
    
    l_c_area = 0
    if len(shapeDict['c']) > 0:
        for i in range(len(shapeDict['c'])):
            tmp_area = Circle(shapeDict['c'][i]).area()
            if l_c_area < tmp_area:
                l_c_area = tmp_area
        #print l_c_area
        inp = round(math.sqrt(l_c_area / math.pi), 1)
        res += (Circle(inp),)
    
    tr_area_list = []
    if len(shapeDict['t']['b']) > 0:
        for i in range(len(shapeDict['t']['b'])):
            tmp_area = Triangle(shapeDict['t']['b'][i], shapeDict['t']['h'][i]).area()
            tr_area_list.append((tmp_area, i))
        tr_area_list.sort(reverse=True)
        ar = [c[0] for c in tr_area_list]
        if ar.count(ar[0]) >= 1:
            ar_count = ar.count(ar[0])
            tr_area_list = tr_area_list[:ar_count]
        for i in range(ar_count):
            ir = tr_area_list[i][1]
            res += ((Triangle(shapeDict['t']['b'][ir], shapeDict['t']['h'][ir])),)
        #print tr_area_list
    if len(res) > 0:
        return res
        
        
## TO DO

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    instShapeSet = ShapeSet()
    for line in open(filename):
        line = line.strip().split(',')
        #print line
        if line[0].lower() == 'square':
            in_list = instShapeSet.shapeSet['s']
            in_list.append(float(line[-1]))
        if line[0].lower() == 'circle':
            in_list = instShapeSet.shapeSet['c']
            in_list.append(float(line[-1]))
        if line[0].lower() == 'triangle':
            in_list = instShapeSet.shapeSet['t']
            in_list['b'].append(float(line[-2]))
            in_list['h'].append(float(line[-1]))
    in_list = []            # garbage
    return instShapeSet

if __name__ == '__main__':
    ss = readShapesFromFile('shapes.txt')
    print ss
    largest = findLargest(ss)
    print
    for item in largest:
        print item
    
    