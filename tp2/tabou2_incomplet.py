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

C = {5: 0, 9: 1, 0: 2, 1: 1, 6: 0, 3: 2, 2: 1, 4: 2, 8: 0, 7: 0}

def colorReduction(graph, coloration): 
    colorationReduced = copy.deepcopy(coloration)
    maxColorUsed = max(coloration.values())
    #print('Nb color used: ', numberOfColorUsed)
    for vertice in coloration.keys(): 
        if(coloration[vertice] == maxColorUsed):
            colorationReduced[vertice] = getColorWithMinConflict(vertice, graph, copy.deepcopy(coloration))
    return colorationReduced

def getColorWithMinConflict(vertice, graph, coloration): 
    currentColor = coloration[vertice]
    newColoration = copy.deepcopy(coloration)
    minNumberOfConflicts = float('inf')

    for i in range(currentColor - 1, -1, -1): # TODO: ici jai change, c'etait : range(currentColor - 1, 0, -1):
        newColoration[vertice] = i
        nbOfConflict = getNumberOfConflict(graph, copy.deepcopy(newColoration))
        if(nbOfConflict < minNumberOfConflicts):
            minNumberOfConflicts = nbOfConflict
            currentColor = i
    return currentColor

def getNumberOfConflict(graph, coloration):
    nbOfConflict = 0
    for vertice in graph.keys():
        for neighbour in graph[vertice]: 
            if(coloration[vertice] == coloration[neighbour]):
                nbOfConflict += 1
    return nbOfConflict / 2

def tabou2(graph): 
    coloration = glutton(graph)
    #print('Result glouton : ')
    #printOrderedDict(coloration)
    newColorationWithoutConflict = coloration
    lastColoration = {}
    
    nbOfUniqueColors = Helper.findNbOfUniqueColorsInSolution(coloration)
    candidateColorationPossiblyConflicted = colorReduction(graph, coloration)
    
    #tabou search
    bestColoration = []
    tabouList = []
    currentColoration = []
    
    #generation de voisins
    
    
    
    newColorationWithoutConflict = coloration
    lastColoration = {}
    
    
def tabouSearch(graph, coloration): 
    bestColoration = coloration
    currentColoration = coloration
    #print('Coloration color init:')
    #printOrderedDict(currentColoration)
    tabouList = []
    nbOfIterations = 1
    nbConflictBest = getNumberOfConflict(graph, bestColoration)

    while nbConflictBest > 0 and nbOfIterations < 100: #TODO: Check if is the good number of iterations (analyse)
        for vertice in currentColoration.keys():
            initialColor = currentColoration[vertice]
            #print('Coloration before neighbour generation for node :', vertice)
            #printOrderedDict(currentColoration)
            currentColoration = getBestNeighbour(graph, vertice, copy.deepcopy(currentColoration), tabouList) #Génération voisins et choix
            #print('Coloration after neighbour generation for node :', vertice)
            #printOrderedDict(currentColoration)
            nbConflictCurrent = getNumberOfConflict(graph, copy.deepcopy(currentColoration))
            nbConflictBest = getNumberOfConflict(graph, copy.deepcopy(bestColoration))
            #print('nb conflict new :', nbConflictCurrent)
            #print('nb conflict best :', nbConflictBest)

            timeInTabouList = 2*nbConflictCurrent + randrange(1,10)
            coupleAlreadyInTabou = False
            for couple in tabouList:
                if couple[0] == vertice:
                    if couple[1] == initialColor:
                        coupleAlreadyInTabou = True
            if not coupleAlreadyInTabou:
                tabouList.append([vertice, initialColor, timeInTabouList]) #Ajout a la liste tabou
            #print('tabou list :', tabouList)


            if nbConflictCurrent < nbConflictBest: 
                bestColoration = copy.deepcopy(currentColoration) #Comparaison avec la meilleure coloration
        for couple in tabouList:
            couple[2] -= 1 #Decremente le temps dans la liste tabou
            if (couple[2] == 0):
                #print('remove in tabou;', couple)
                tabouList.remove(couple)
        #print(tabouList)

        nbOfIterations += 1
        #print('nb iteration: ', nbOfIterations)
    return bestColoration

def getBestNeighbour(graph, vertice, coloration, tabouList):
    numberOfColorsAvailable = max(coloration.values()) + 1
    colorsInTabouList = []
    for couple in tabouList:
        if (couple[0] == vertice):
            colorsInTabouList.append(couple[1])
    minNumberOfConflicts = float('inf')
    newColoration = copy.deepcopy(coloration)

    for i in range(numberOfColorsAvailable - 1, -1, -1): # TODO: ici change 0 a -1
        if(i != coloration[vertice] and i not in colorsInTabouList):
            newColoration[vertice] = i
            nbOfConflict = getNumberOfConflict(graph, copy.deepcopy(newColoration))
            if(nbOfConflict < minNumberOfConflicts):
                minNumberOfConflicts = nbOfConflict
    #printOrderedDict(newColoration)
    return newColoration
