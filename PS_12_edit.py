# 6.00 Problem Set 12
#
# Name: CMLilley
# Collaborators: none
# Time:

import numpy
import random
import pylab
import copy

class NoChildException(Exception):pass
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """  
#
# PROBLEM 1
#

class SimpleVirus(object):

    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        
    def doesClear(self):
        return random.random() <= self.clearProb
    
    def reproduce(self, popDensity):        
        if random.random() <= self.maxBirthProb * (1 - popDensity):
                return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
                raise NoChildException()


class SimplePatient(object):
    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        return len(self.viruses)      

    def update(self):
        virIndex = copy.copy(self.viruses)  #shallow copy, so same items in each list
        for i in virIndex:
            if i.doesClear():
                self.viruses.remove(i)
        density = float(self.getTotalPop()) / float(self.maxPop)
        virIndex = copy.copy(self.viruses)  #shallow copy, so same items in each list
        for i in virIndex:
            try:
                self.viruses.append(i.reproduce(density))
            except NoChildException:
                pass    
        return self.getTotalPop()

#
# PROBLEM 2
#

def problem2():
    numViruses = 100
    maxTime = 300
    viruses = [SimpleVirus(0.1, 0.05) for i in range(numViruses)]
    
    patient = SimplePatient(viruses ,1000)
    time = 0
    popNums = []
    
    while time < maxTime:
        popNums.append(patient.update())
        time += 1

    pylab.figure()
    pylab.plot(popNums, '-r')
    pylab.axis([-5, 310, 350, 1010])
    pylab.ylabel ('Population Size')
    pylab.xlabel ('Time elapsed')
    pylab.title ('SimpleVirus population size over time, w/o drugs')
    
    pylab.show()
    
# problem2()
#### Problem2 comments: pop stabilizes at about 500 in 50 ticks or so, because clearance rate now equals reproduction rate

#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)  # be sure to use parent __init__ method

        self.resistances = resistances
        self.mutProb = mutProb
        
    def getResistance(self, drug):
        return self.resistances[drug]
        
    def reproduce(self, popDensity, activeDrugs):
        resistable = [self.getResistance(i) for i in activeDrugs] 
        if False not in resistable:                                     # if it doesn't lack key resistance
            if random.random() <= self.maxBirthProb * (1 - popDensity): # and if allowed to reproduce by density
                newResistances = self.resistances.copy()    #make copy of resistances
                for i in newResistances:                    #iterate through them
                    if random.random() <= self.mutProb:     #and change if you hit mutProb
                        if newResistances[i] == True: 
                            newResistances[i] = False
                        else:
                            newResistances[i] = True
                return ResistantVirus(self.maxBirthProb, self.clearProb, newResistances, self.mutProb)
            else:
                raise NoChildException()
        else:
            raise NoChildException()
            
class Patient(SimplePatient):

    def __init__(self, viruses, maxPop):
        SimplePatient.__init__(self, viruses, maxPop)     
        self.activeDrugs = []
        
    def addPrescription(self, newDrug):
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)

    def getPrescriptions(self):
        return self.activeDrugs
        
    def getResistPop(self, drugResist):
        resisters = copy.copy(self.viruses)
        for i in drugResist:            
            for v in self.viruses:
                if v.resistances[i] == False and v in resisters:
                    resisters.remove(v)
        return len(resisters)

    def update(self):
        virIndex = copy.copy(self.viruses)  #shallow copy, so same items in each list
        for i in virIndex:
            if i.doesClear():
                self.viruses.remove(i)
        density = float(self.getTotalPop()) / float(self.maxPop)
        virIndex = copy.copy(self.viruses)  #shallow copy, so same items in each list
        for i in virIndex:
            try:
                self.viruses.append(i.reproduce(density, self.activeDrugs))
            except NoChildException:
                pass
        return self.getTotalPop()
#
# PROBLEM 4
#

def problem4():
    numViruses = 100
    viruses = [ResistantVirus(0.1, 0.05, {'guttagonol':False}, .005) for i in xrange(numViruses)] # list comprehension
    patient = Patient(viruses,1000)
    time = 0
    timetodrug = 10
    timetoend = timetodrug + 150
    popNums = []
    resistNums = []
    while time <= timetodrug:
        popNums.append(patient.update())
        time += 1  
    patient.addPrescription('guttagonol')
    while time <= timetoend:
        popNums.append(patient.update())
        resistNums.append( patient.getResistPop(patient.getPrescriptions()) )
        time += 1
    pylab.figure()
    pylab.plot(popNums, '-r', label = 'Total Population')
    if resistNums[-1] > 0:
        pylab.plot(xrange(timetodrug+1,timetoend+1), resistNums, '-b', label = 'Resistant Population')
        pylab.legend()
    pylab.axis([-5, timetoend+5, -5, 600])
    pylab.ylabel ('Population Size')
    pylab.xlabel ('Time elapsed')
    pylab.title ('ResistantVirus pop over time, w/ Guttagonol added after ' + str(timetodrug) + ' ticks')
    pylab.axvline (x=timetodrug, linestyle = '--')
    
    print "Highest population of resistant bugs was: " + str(resistNums[-1])
    pylab.show()
# problem4()
"""PROBLEM 4 NOTES: If mutation begins immediately, without requiring presence of drug, then total
population falls quickly after drug introduced, stabilizes as resistant viruses become ever larger
part of population, then begins growing again as resistant viruses dominate. Only if drug introduced
by tick 10 or so is resistance usually prevented and virus wiped out.""" 

#
# PROBLEM 5
#
        
def problem5():
    numViruses = 100
    numSimulations = 30
    timetodrug = [0, 10, 25, 75, 150, 300]
    avgList = [] 
    # To cycle through the given configurations:
    for i in range (len(timetodrug)):
        drugtime = timetodrug[i]
    # To run N number of simulations with a given configuration:
        seriesList = []
        timetoend = drugtime + 150
        for n in range (numSimulations):
            viruses = [ResistantVirus(0.1, 0.05, {'guttagonol':False}, .005) for i in range(numViruses)]
            patient = Patient(viruses,1000)
            time = 0
            popNums = []
            while time <= drugtime:
                popNums.append(patient.update())
                time += 1
            patient.addPrescription('guttagonol')
            while time <= timetoend:
                popNums.append(patient.update())    # List for the simulation
                time += 1            
            seriesList.append(popNums[-1])  #list for that series/configuration. Saves only final population size.
        
        pylab.figure()
        pylab.hist (seriesList)
        pylab.yticks(range(10)) 
        pylab.ylabel ('Number of patients at final pop.')
        pylab.xlabel ('Final Population Size')
        titletext = 'ResistantVirus final pops, for treatment delay of ' + str(drugtime) + ' ticks.'
        pylab.title (titletext)
        print "Series complete, for " + str(drugtime) + " ticks of delay."
    pylab.show()

# problem5()
### PROBLEM 5 COMMENTS: No patients are cured at 150 or 300. For 75 ticks delay, 13% were cured. 
### For 25 ticks delay, 50-75% were cured (This proportion varied most across multiple runs. 
### For 10 delay, 80%. For 0 delay, all patients are cured. This corresponds to the length of 
### time the virus has in which to develop resistance. 

#
# PROBLEM 6
#

def problem6():
    numViruses = 100
    numSimulations = 100
    timetodrug = [0, 10, 25, 75, 150, 300]
    # To cycle through the given configurations:
    for i in range (len(timetodrug)):
        drugtime = timetodrug[i]
    # To run N number of simulations with a given configuration:
        seriesList = []
        timetoend = 150 + drugtime + 150
        for n in range (numSimulations):
            viruses = [ResistantVirus(0.1, 0.05, {'guttagonol':False, 'grimpex':False}, .005) for i in range(numViruses)]
            patient = Patient(viruses,1000)
            time = 0
            popNums = []  
            while time < 150:
                popNums.append(patient.update())
                time += 1
            patient.addPrescription('guttagonol')
            while time < drugtime + 150:
                popNums.append(patient.update())
                time += 1
            patient.addPrescription('grimpex')
            while time < timetoend:
                popNums.append(patient.update())    # List for the simulation
                time += 1
            seriesList.append(popNums[-1])  #list for that series/configuration. Saves only final population size.
            print "Total time elapsed this Simulation: " + str(time) + " ticks."
            
        pylab.figure()
        pylab.hist (seriesList)
        # pylab.yticks(range(20)) 
        pylab.ylabel ('Number of patients at final pop.')
        pylab.xlabel ('Final Population Size')
        titletext = 'Final pops, for delay of ' + str(drugtime) + ' ticks before 2nd drug.'
        pylab.title (titletext)
        print "Series complete, for " + str(drugtime) + " ticks of delay."
    pylab.show()
# problem6()

### PROBLEM 6 NOTES: There is considerable stochastic variability in results, so I was forced to 
### run 100 trials per configuration. At that sample size, a trend-line becomes clearer. Even at 0 
### ticks delay, there is a chance for enough viruses to acquire immunity to both drugs during the 
### first 150 ticks before either drug is introduced, so about 11% of patients remain infected. For 
### 10-150 ticks delay, cure rate gradually falls through 81 to 69 to 53 percent, then more abruptly 
### to 17, then 6. At this delay, we're guaranteeing that grimpex resistance develops fully before 
### grimpex is added. 



#
# PROBLEM 7
#
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length. (Borrowed from a previous 6.00 assignment)
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

def problem7():

    numViruses = 100
    numSimulations = 1
    timetodrug = [0, 300]
    avgList = []
    
    # To cycle through the given configurations:
    for i in range (len(timetodrug)):
        drugsdelay = timetodrug[i]
        timetoend = 150 + drugsdelay + 150
    
    # To run N number of simulations with a given configuration:
        seriesPops = []
        seriesResist = []
        seriesGutt = []
        seriesGrim = []
        
        for n in range (numSimulations):
            viruses = [ResistantVirus(0.1, 0.05, {'guttagonol':False, 'grimpex':False}, .005) for i in range(numViruses)]
            patient = Patient(viruses,1000)
            time = 0
            popNums = []
            guttResist = []
            grimResist = []
            bothResist = []
            
            while time < 150:
                popNums.append(patient.update())
                bothResist.append(patient.getResistPop(['guttagonol', 'grimpex']))
                guttResist.append(patient.getResistPop(['guttagonol',]))
                grimResist.append(patient.getResistPop(['grimpex',]))
                time += 1
            patient.addPrescription('guttagonol')
            while time < drugsdelay + 150:
                popNums.append(patient.update())
                bothResist.append(patient.getResistPop(['guttagonol', 'grimpex']))
                guttResist.append(patient.getResistPop(['guttagonol',]))
                grimResist.append(patient.getResistPop(['grimpex',]))
                time += 1
            patient.addPrescription('grimpex')
            while time < timetoend:
                popNums.append(patient.update())    # List for the simulation
                bothResist.append(patient.getResistPop(['guttagonol', 'grimpex']))
                guttResist.append(patient.getResistPop(['guttagonol',]))
                grimResist.append(patient.getResistPop(['grimpex',]))
                time += 1
            
            print "For this trial, total pop was " + str(popNums[-1]) + ", bothResist was " + str(bothResist[-1]) + ", guttResist was "  + str(guttResist[-1]) + ", and grimResist was "  + str(grimResist[-1])
            seriesPops.append(popNums)
            seriesResist.append(bothResist)
            seriesGutt.append(guttResist)
            seriesGrim.append(grimResist)
        
        popMeans = computeMeans(seriesPops)
        resistMeans = computeMeans(seriesResist)
        guttMeans = computeMeans(seriesGutt)
        grimMeans = computeMeans(seriesGrim)
        
        print "Series complete for delay of " + str(drugsdelay)
        
        pylab.figure()
        pylab.plot(popMeans, '-r', label = 'Total Pop')
        pylab.plot(resistMeans, '-b', label = 'Dual-Resistant Pop')
        pylab.plot(guttMeans, '-g', label = 'Guttagonol-Resistant')
        pylab.plot(grimMeans, '-y', label = 'Grimpex-Resistant')
            
        pylab.axis([-5, timetoend+5, -5, 700])
        pylab.ylabel ('Population Size')
        pylab.xlabel ('Time elapsed')
        pylab.title ('ResistantVirus pop: Guttagonol added @ 150, Grimpex @ ' + str(drugsdelay+150) + ' ticks')
        pylab.axvline (x=drugsdelay+150, linestyle = '--')
        pylab.axvline (x=150, linestyle = '--')
        pylab.legend()
    pylab.show()
problem7()
