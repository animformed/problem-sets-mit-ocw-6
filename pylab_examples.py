from pylab import *
import random

plot([1, 2, 3, 4])         # when not instructed explicitly, plot assumes x axis from 0 as 0, 1, 2, 3. These four values in list are y values
plot([5, 6, 7, 8])
plot([1, 2, 3, 4],[1, 4, 9, 16])        # with x and y axis values (x, y)

figure()                     # create a new figure, instead of putting the plot in the same figure
plot([1, 2, 3, 4],[1, 4, 9, 16],'ro')       # plot with red circle markers
axis([0, 6, 0, 20])         # specifying the length of display axes; x from 0 to 6, y from 0 to 20
title('Earnings')            # title of the figure
xlabel('Days')                # x and y axis labels
ylabel('Dollars')

figure()
xAxis = array([1, 2, 3, 4])     # create an array. Can use standard operations on array objects
print xAxis
test = arange(1, 5)             # gives you an array of ints, not a list
print test
print test == xAxis
yAxis = xAxis**3                # not possible if xAxis was a list.
plot(xAxis, yAxis, 'ro')
title('x and y')
axis([0, 5, 0, 70])

figure()
vals = []
dieVals = [1, 2, 3, 4, 5, 6]
for i in range(10000):
    vals.append(random.choice(dieVals) + random.choice(dieVals))
hist(vals, bins = 11)
show()