# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    subInfo = {}
    inputFile = open(filename)
    for line in inputFile:
        name, value, hours = line.strip().split(',')
        subInfo[name] = (eval(value), eval(hours)) 
    print'file loaded'
    return subInfo

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    subList = subjects.keys()
    valueList = subjects.values()
    for j in range(len(subList)):
        for i in range(len(subList)-1):
            if comparator(valueList[i], valueList[i+1]):
                tmpVal = valueList[i]
                tmpSub = subList[i]
                valueList[i] = valueList[i+1]
                subList[i] = subList[i+1]
                valueList[i+1] = tmpVal
                subList[i+1] = tmpSub
    
    count = 0
    res = {}
    for i in range(len(subList)-1, -1, -1):
        #print count, i
        res[subList[i]] = valueList[i]
        count += valueList[i][WORK]
        if count > maxWork:                 # if maxWork suddenly increases because of a large work increment
            count -= valueList[i][WORK]
            res.pop(subList[i])
            break
        
    return res
            
        
                 
    
    # TODO...

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    #print bestSubset, bestSubsetValue, subset, subsetValue, subsetWork
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            print subset[:], subsetValue, i
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            print 'subset',subset
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue
#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    memo = {}
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            dpAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0, memo)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    global numCalls
    numCalls += 1
    #print bestSubset, bestSubsetValue, subset, subsetValue, subsetWork
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

if __name__ == '__main__':
    numCalls = 0
    sub_dict = loadSubjects(SUBJECT_FILENAME)
#    #print sub_dict
#    printSubjects(sub_dict)
#    g_sub = greedyAdvisor({'6.00':(16, 8), '1.00':(7, 7), '6.01':(5, 3), '15.01':(9, 6)}, 15, cmpValue)
#    printSubjects(g_sub)
#    g_sub = greedyAdvisor({'6.00':(16, 8), '1.00':(7, 7), '6.01':(5, 3), '15.01':(9, 6)}, 15, cmpWork)
#    printSubjects(g_sub)
#    g_sub = greedyAdvisor({'6.00':(16, 8), '1.00':(7, 7), '6.01':(5, 3), '15.01':(9, 6)}, 15, cmpRatio)
#    printSubjects(g_sub)
#    g_sub = greedyAdvisor(sub_dict, 20, cmpValue)
#    printSubjects(g_sub)
#    g_sub = greedyAdvisor(sub_dict, 20, cmpWork)
#    printSubjects(g_sub)
#    g_sub = greedyAdvisor(sub_dict, 20, cmpRatio)
#    printSubjects(g_sub)
    
    g_sub = bruteForceAdvisor({'6.00':(16, 8), '1.00':(7, 7), '6.01':(5, 3), '15.01':(9, 6), '4.00':(4,11),'4.01':(2,5),'4.02':(5,13),'4.03':(6,16),'4.04':(3,7),'4.05':(7,13),'4.06':(7,15)}, 15)
#    printSubjects(sub_dict)
    print 'BruteForceAdvisor'
#    g_sub = bruteForceAdvisor(sub_dict, 6)
    printSubjects(g_sub)
#    print 'numcalls:',numCalls
   