# scriptGenerator.py
# the basics for Heather Anne Campbell's Magic Sketch Macine

from numpy import random
import sys
import random

#global unpopulated lists

jobsList = []
adjList = []
placeList = []
celebList = []

#this function populates the lists

def incrementList(list):
    for i in range (0,10):
        userin = input("Please enter word #" + str(i + 1) +"\n")
        list.append(userin)
        print(list)

# prompt user for what type of list, then create lists

print("Create a list of jobs.")
incrementList(jobsList)
print("Create a list of adjectives.")
incrementList(adjList)
"""print("Create a list of places and times.")
placeList = createList()
print("Create a list of celebrities and characters.")
celebList = createList()
"""

#DICTIONARY METHOD? FOR RANDOM VALUES LATER
#this indexes the lists for random selection
#listDict = {1:jobsList,2:adjList,3:placeList,4:celebList}
#
#listDict.get(random.randint(0,len(listDict)))
#TODO: randomly pop value out of list, into new list of combinations

#this function randomly returns a list value, then removes it from the original list
def randomGrab(list):
    while len(list) > 0:
        return_value = random.choice(list)
        list.remove(return_value)
        return return_value

#this is the list of combined words
    
pitches = []

#this function combines two strings and returns the new value

def combine(var1,var2):
    pitches.append( str(var1) + ' ' + str(var2) )
    return pitches

#this function takes grabs two lists, then combines those words 10 times

def pitchCombiner(list,list2):
    for i in range (0,10):
        wordOne = randomGrab(list):
        wordTwo = randomGrab(list2):
        combine(wordOne, wordTwo)

pitchCombiner(jobsList, adjList)
print (pitches)

