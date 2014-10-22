# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words2.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def ghost():
    
    def l_input(i_word, i_turn):
        print "\nCurrent word fragment: '%s'" % i_word.upper()
        print "Player %s's turn." % i_turn
        i_inp = raw_input('Player {0} says letter: '.format(i_turn))
        return i_inp
    
    def word_check(i_word):
        flag = 1
        word_len = len(i_word)
        #words = load_words()
        
        if i_word.lower() in wordlist:
            flag = 2
            return flag
                               
        for item in wordlist:
            #print item
            if i_word.lower() == item[slice(None, word_len)]:
                break
        else:
            flag = 3
            return flag
        
        return flag
            
    en_flag = 1
    turn = 1
    word = ''
    print '\nWelcome to Ghost!'
    print 'Player 1 goes first.'
    print "Current word fragment: ''"
    inp = raw_input('Player 1 says letter: ')
    
    while(en_flag == 1):
        if inp.isdigit() or len(inp) > 1:
            print 'Wrong Input.'
            inp = l_input(word, turn)
            continue
        word += inp
        en_flag = word_check(word)
        if en_flag > 1:
            break
        if turn == 1:
            turn = 2
            inp = l_input(word, turn)
            continue
        if turn == 2:
            turn = 1
            inp = l_input(word, turn)
            continue
        
    if en_flag == 2:
        print "\nCurrent word fragment: '%s'" % word.upper()
        print "Player {0} loses because '{1}' is a word!".format(turn, word)
        if turn == 1:
            print 'Player 2 wins!'
        else:
            print 'Player 1 wins!'
        
    if en_flag == 3:
        print "\nCurrent word fragment: '%s'" % word.upper()
        if turn == 1:
            print "Player 1 loses because no word begins with '%s'!" % word
            print 'Player 2 wins!'
        else:
            print "Player 2 loses because no word begins with '%s'!" % word
            print 'Player 1 wins!'

ghost()
        
        
            
        
                
                    
            
            
        
    
    
