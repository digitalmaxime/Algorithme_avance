from glutton import glutton
from graph import Helper
from random import randrange
import copy
from branch_and_bound import branch_bound
from read_file import Build_adjacent_list_graph, Build_graph
from tabou3 import tabucol

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

def tabou(graph): 
    coloration = glutton(graph)
    newColorationWithoutConflict = coloration
    lastColoration = {}

    #Loop between colorReduction and tabouSearch until tabouSearch fails
    while (lastColoration != newColorationWithoutConflict): 
        lastColoration = copy.deepcopy(newColorationWithoutConflict)
        newColorationWithConflict = colorReduction(graph, copy.deepcopy(newColorationWithoutConflict))
        resultTabou = tabouSearch(graph, copy.deepcopy(newColorationWithConflict))
        print('-' * 40)
        print(resultTabou)
        print('-' * 40)
        numberOfConflictTabou = getNumberOfConflict(graph, copy.deepcopy(resultTabou))

        if (numberOfConflictTabou > 0): 
            newColorationWithoutConflict = lastColoration
            print('newColorationWithoutConflict = lastColoration')
        else: 
            newColorationWithoutConflict = resultTabou
            print('newColorationWithoutConflict = resultTabou')
            
    return newColorationWithoutConflict

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

    return bestColoration


def getBestNeighbour(graph, vertice, coloration, tabouList):
    numberOfColorsAvailable = max(coloration.values()) + 1
    colorsInTabouList = []
    for couple in tabouList: #Worst case : O(V*(K-1))
        if (couple[0] == vertice):
            colorsInTabouList.append(couple[1])
    minNumberOfConflicts = float('inf')
    newColoration = copy.deepcopy(coloration)
    originalNewColoration = copy.deepcopy(coloration)
    #print('colors in tabou list for vertice :', vertice)
    #print(colorsInTabouList)
    bestTuple= tuple()
    
    for i in range(numberOfColorsAvailable - 1, -1, -1): #O(K-1)
        newColoration = copy.deepcopy(originalNewColoration)
        if(i != coloration[vertice] and i not in colorsInTabouList):
            newColoration[vertice] = i
            nbOfConflict = getNumberOfConflict(graph, copy.deepcopy(newColoration)) #O(V²)
            if(nbOfConflict < minNumberOfConflicts):
                minNumberOfConflicts = nbOfConflict
                bestTuple = (vertice, i)
                
    if bestTuple != ():
        originalNewColoration[bestTuple[0]] = bestTuple[1]
    #printOrderedDict(newColoration)
    return originalNewColoration


#Worst case : Theta(V⁴)
def colorReduction(graph, coloration): 
    colorationReduced = copy.deepcopy(coloration)
    numberOfColorUsed = max(coloration.values()) + 1

    for vertice in coloration.keys(): 
        if(coloration[vertice] == numberOfColorUsed - 1):
            colorationReduced[vertice] = getColorWithMinConflict(vertice, graph, copy.deepcopy(colorationReduced)) # TODO: ici chage coloration a colorationReduced
    return colorationReduced

#Worst case : Theta(V²)
def getNumberOfConflict(graph, coloration): 
    nbOfConflict = 0
    for vertice in graph.keys():
        for neighbour in graph[vertice]: 
            if(coloration[vertice] == coloration[neighbour]):
                nbOfConflict += 1
    return nbOfConflict / 2

#Theta((K-1)*(V²))  
def getColorWithMinConflict(vertice, graph, coloration): 
    currentColor = coloration[vertice]
    newColoration = copy.deepcopy(coloration)
    minNumberOfConflicts = float('inf')

    for i in range(currentColor - 1, 0, -1):
        newColoration[vertice] = i
        nbOfConflict = getNumberOfConflict(graph, copy.deepcopy(newColoration))
        if(nbOfConflict <= minNumberOfConflicts):
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
    
    (graph1, num) = Build_graph("./generated_files/gen_ex40_0")
    graph2 = Build_adjacent_list_graph("./instances/ex40_0")
    
    colorationGlutton = glutton(graph1)
    print('Result glouton : ')
    printOrderedDict(colorationGlutton)
    print(Helper.findNbOfUniqueColorsInSolution(colorationGlutton))
    
    colorationBranch = branch_bound(graph1)
    print('Result branch : ')
    printOrderedDict(colorationBranch)
    print(Helper.findNbOfUniqueColorsInSolution(colorationBranch))
    
    colorationTabou = tabou(graph1)
    print('Result tabou : ')
    printOrderedDict(colorationTabou)
    print(Helper.findNbOfUniqueColorsInSolution(colorationTabou))
    
    
    # colorationTabou3 = tabucol(graph2, 23)
    # print('Result tabou3 : ')
    # printOrderedDict(colorationTabou3)
    # print(Helper.findNbOfUniqueColorsInSolution(colorationTabou3))
    
    
    
    
    
    #bestCol = tabouSearch(G10_3, C)
    #print('FINAL')
    #printOrderedDict(bestCol)
    #print('new coloration with conflict :')
    #printOrderedDict(C)
    #getBestNeighbour(G10_3, 2, C, [])

    #result = tabou(G10_3)
    #printOrderedDict(result)
    #sortedResult = dict(sorted(result.items()))
    #for val in sortedResult.values() :
        #print(val, end=" ")
    #print()
    #print("*" * 40)