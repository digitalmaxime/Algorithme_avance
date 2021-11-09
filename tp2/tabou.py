from glutton import glutton
from graph import Helper
from random import randrange
import copy

G = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["b", "c", "e"],
   "e" : ["d"]
}

G10_3 = {0: [1,3,5,9], 1:[0,5,6,8], 2:[4,5,6,8], 3:[0,6,9], 4:[2,5,7,8], 5:[0,1,2,4,9], 6:[1,2,3,9], 7:[4,9], 8:[1,2,4], 9:[0,3,5,6,7]}

G1 = {0: [3], 1: [2, 3, 4], 2: [1, 3], 3: [0, 1, 2], 4: [1]}

C = {
    "a": 0,
    "b": 2,
    "c": 1,
    "d": 0,
    "e": 1
}

def tabou(graph): 
    coloration = glutton(graph)
    print('Result glouton : ')
    printOrderedDict(coloration)
    newColorationWithoutConflict = coloration
    lastColoration = {}

    #Loop between colorReduction and tabouSearch until tabouSearch fails
    while (lastColoration != newColorationWithoutConflict): 
        lastColoration = copy.deepcopy(newColorationWithoutConflict)
        newColorationWithConflict = colorReduction(graph, copy.deepcopy(newColorationWithoutConflict))
        print('new coloration with conflict :')
        printOrderedDict(newColorationWithConflict)
        resultTabou = tabouSearch(graph, newColorationWithConflict)
        print('result tabou :')
        printOrderedDict(resultTabou)
        numberOfConflictTabou = getNumberOfConflict(graph, resultTabou)
        print('conflict : ', numberOfConflictTabou)
        if (numberOfConflictTabou > 0): 
            newColorationWithoutConflict = lastColoration
        else: 
            newColorationWithoutConflict = resultTabou
    return newColorationWithoutConflict

def tabouSearch(graph, coloration): 
    bestColoration = coloration
    currentColoration = coloration
    tabouList = []
    nbOfIterations = 1
    nbConflictBest = getNumberOfConflict(graph, bestColoration)

    while (nbConflictBest > 0 | nbOfIterations < 50): #TODO: Check if is the good number of iterations (analyse)
        for vertice in currentColoration.keys():
            initialColor = currentColoration[vertice]
            currentColoration = getBestNeighbour(graph, vertice, currentColoration, tabouList) #Génération voisins et choix
            #print('Coloration after neighbour generation :', currentColoration)
            nbConflictCurrent = getNumberOfConflict(graph, currentColoration)
            nbConflictBest = getNumberOfConflict(graph, bestColoration)

            timeInTabouList = 2*nbConflictCurrent + randrange(1,10)
            tabouList.append([vertice, initialColor, timeInTabouList]) #Ajout a la liste tabou
            #print('tabou list :', tabouList)

            if nbConflictCurrent < nbConflictBest: 
                bestColoration = currentColoration #Comparaison avec la meilleure coloration
        for couple in tabouList:
            couple[2] -= 1 #Decremente le temps dans la liste tabou
            if (couple[2] == 0):
                tabouList.remove(couple)

        nbOfIterations += 1
    return bestColoration

def getBestNeighbour(graph, vertice, coloration, tabouList):
    numberOfColorsAvailable = max(coloration.values()) + 1
    colorsInTabouList = []
    for couple in tabouList:
        if (couple[0] == vertice):
            colorsInTabouList.append(couple[1])
    minNumberOfConflicts = float('inf')
    newColoration = coloration

    for i in range(numberOfColorsAvailable - 1, 0, -1):
        if(i != coloration[vertice] & i not in colorsInTabouList):
            newColoration[vertice] = i
            nbOfConflict = getNumberOfConflict(graph, newColoration)
            if(nbOfConflict < minNumberOfConflicts):
                minNumberOfConflicts = nbOfConflict
    return newColoration


def colorReduction(graph, coloration): 
    colorationReduced = coloration
    numberOfColorUsed = max(coloration.values()) + 1
    #print('Nb color used: ', numberOfColorUsed)
    for vertice in coloration.keys(): 
        if(coloration[vertice] == numberOfColorUsed - 1):
            colorationReduced[vertice] = getColorWithMinConflict(vertice, graph, coloration)
    return colorationReduced

def getNumberOfConflict(graph, coloration): 
    nbOfConflict = 0
    for vertice in graph.keys():
        for neighbour in graph[vertice]: 
            if(coloration[vertice] == coloration[neighbour]):
                nbOfConflict += 1
    return nbOfConflict / 2
    
def getColorWithMinConflict(vertice, graph, coloration): 
    currentColor = coloration[vertice]
    newColoration = coloration
    minNumberOfConflicts = float('inf')

    for i in range(currentColor - 1, 0, -1):
        newColoration[vertice] = i
        nbOfConflict = getNumberOfConflict(graph, newColoration)
        if(nbOfConflict < minNumberOfConflicts):
            minNumberOfConflicts = nbOfConflict
            currentColor = i
    return currentColor

def printOrderedDict(result):
    sortedResult = dict(sorted(result.items()))
    for val in sortedResult.values() :
        print(val, end=" ")
    print()
    print("*" * 40)

if __name__ == "__main__":
    result = tabou(G10_3)
    printOrderedDict(result)
    #sortedResult = dict(sorted(result.items()))
    #for val in sortedResult.values() :
        #print(val, end=" ")
    #print()
    #print("*" * 40)