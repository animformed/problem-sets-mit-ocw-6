# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

class NoChildException(Exception):
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
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = float(maxBirthProb)
        self.clearProb = float(clearProb)
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        return random.random() <= self.clearProb        # check if within the prob threshold
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        if random.random() <= self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException, 'Cannot reproduce a child virus.'
            

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        return len(self.viruses)        

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """
        #print 'Viruses in SimplePatient updating...'
        update_viruses = []                     # temporarily stores updated SimpleVirus list
        for item in self.viruses:               # checks if doesClear(), virus is cleared from body
            if not item.doesClear():
                update_viruses.append(item)
        self.viruses = update_viruses           # get the updated SimpleVirus list
        
        
        popDensity = self.getTotalPop()/float(self.maxPop)
        new_viruses = []
        for item in self.viruses:               # reproduce and temporarily create a list for new SimpleViruses
            try:
                new_viruses.append(item.reproduce(popDensity))
            except NoChildException as exp:
                pass
                #print exp.args[0]               # printing exception argument value
        self.viruses.extend(new_viruses)        # Add new SimpleViruses to the SimpleVirus list
        return self.getTotalPop()
                

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    new_vlist = []
    for i in xrange(100):
        new_vlist.append(SimpleVirus(0.1, 0.05))
    sp = SimplePatient(new_vlist, 1000)
    #print sp.getTotalPop()
    
    pop = []
    for i in xrange(300):
        pop.append(sp.update())
        
    pylab.figure()
    pylab.plot(pop)
    pylab.title('Population of SimpleVirus in SimplePatient in 300 Timesteps')
    pylab.xlabel('Timesteps')
    pylab.ylabel('SimpleVirus growth')
    
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex':False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        self.maxBirthProb = float(maxBirthProb)
        self.clearProb = float(clearProb)
        self.resistances = resistances
        self.mutProb = float(mutProb)
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances[drug]
        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        check = True
        new_resistances = {}
        
        for drug in activeDrugs:  
                if not self.getResistance(drug):
                    check = False
                    break
        else:
            check = True
        if check:
            if random.random() <= self.maxBirthProb * (1 - popDensity):
                for key in self.resistances:
                    new_resistances[key] = False
                    if self.resistances[key]:
                        if random.random() <= self.mutProb:
                            new_resistances[key] = False
                    if not self.resistances[key]:
                        if random.random() <= self.mutProb:
                            new_resistances[key] = True
                  
                return ResistantVirus(self.maxBirthProb, self.clearProb, new_resistances, self.mutProb)
            else:
                raise NoChildException, 'Cannot reproduce a child virus.'
        else:
            raise NoChildException, 'Cannot reproduce a child virus. Not resistant to drug.'
                
                
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        ResistantVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.admDrugs = []
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if not newDrug in self.admDrugs:
            self.admDrugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.admDrugs
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        count = 0
        for r_virus in self.viruses:
            for drug in drugResist:
                if drug in r_virus.resistances:
                    if r_virus.resistances[drug] == False:
                        break
            else:
                count += 1
        return count

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        #print 'Viruses in Patient updating...'
        update_viruses = []                     # temporarily stores updated SimpleVirus list
        for item in self.viruses:               # checks if doesClear(), virus is cleared from body
            if not item.doesClear():
                update_viruses.append(item)
        self.viruses = update_viruses           # get the updated SimpleVirus list     
        popDensity = self.getTotalPop()/float(self.maxPop)
        new_viruses = []
        for item in self.viruses:               # reproduce and temporarily create a list for new SimpleViruses
            try:
                new_viruses.append(item.reproduce(popDensity, self.admDrugs))
            except NoChildException as exp:
                pass
                #print exp.args[0]               # printing exception argument value
        self.viruses.extend(new_viruses)        # Add new SimpleViruses to the SimpleVirus list
        return self.getTotalPop()

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    nonR_vList = []
    for i in xrange(100):
        nonR_vList.append(ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005))   # create 100 non-guttagonol resistance viruses
           
    sp = Patient(nonR_vList, 1000)      # create a non-drug administered patient
           
    pop = []
    for i in xrange(150):
        pop.append(sp.update())
    
    sp.addPrescription('guttagonol')    # administer drug
    
    for i in xrange(150):
        pop.append(sp.update())
#    
    pylab.figure()
    pylab.plot(pop)
    pylab.title('Population of non-guttagonol resistant viruses in Patient\nbefore and after administering drug at 150th timestep')
    pylab.xlabel('Timesteps')
    pylab.axvline(x=150, linestyle='--', color = 'r')
    pylab.ylabel('Virus growth')

#
# PROBLEM 5
#
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    nonR_vList = []
    for i in xrange(100):
        nonR_vList.append(ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005))   # create 100 non-guttagonol resistance viruses
           
    sp_300 = Patient(nonR_vList, 1000)      # create a non-drug administered patient
    pop_300 = []
    for i in xrange(300):
        pop_300.append(sp_300.update())
    sp_300.addPrescription('guttagonol')    # administer drug
    for i in xrange(150):
        pop_300.append(sp_300.update())
        
    sp_150 = Patient(nonR_vList, 1000)      # create a non-drug administered patient
    pop_150 = []
    for i in xrange(150):
        pop_150.append(sp_150.update())
    sp_150.addPrescription('guttagonol')    # administer drug
    for i in xrange(150):
        pop_150.append(sp_150.update())
        
    sp_75 = Patient(nonR_vList, 1000)      # create a non-drug administered patient
    pop_75 = []
    for i in xrange(75):
        pop_75.append(sp_75.update())
    sp_75.addPrescription('guttagonol')    # administer drug
    for i in xrange(150):
        pop_75.append(sp_75.update())
        
    sp_0 = Patient(nonR_vList, 1000)      # create a non-drug administered patient
    pop_0 = []
    sp_0.addPrescription('guttagonol')    # administer drug
    for i in xrange(150):
        pop_0.append(sp_0.update())
#    
    pylab.figure()
    pylab.plot(pop_300)
    pylab.plot(pop_150)
    pylab.plot(pop_75)
    pylab.plot(pop_0)
    
    pylab.title('Population of non-guttagonol resistant viruses in Patient\nbefore and after administering drug at 150th timestep')
    pylab.xlabel('Timesteps')
    pylab.axvline(x=150, linestyle='--', color = 'r')
    pylab.ylabel('Virus growth')
    
#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO

#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    # TODO
    
if __name__ == '__main__':
    problem2()
    problem4()
    problem5()
    pylab.show()
    
