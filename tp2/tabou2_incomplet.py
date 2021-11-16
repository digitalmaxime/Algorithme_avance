import time
from glutton import glutton
from graph import Helper
from random import randrange
import copy

from branch_and_bound import branch_bound
from read_file import Build_adjacent_list_graph, Build_graph

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
    numberOfColorUsed = Helper.findNbOfUniqueColorsInSolution(colorationReduced)
    
    for vertice in coloration.keys(): 
        if(coloration[vertice] == maxColorUsed):
            color = getColorWithMinConflict(vertice, graph, copy.deepcopy(colorationReduced))  # TODO: ici chage coloration a colorationReduced
            colorationReduced[vertice] = color
    return colorationReduced

def getColorWithMinConflict(vertice, graph, coloration): 
    currentColor = coloration[vertice]
    newColoration = copy.deepcopy(coloration)
    minNumberOfConflicts = float('inf')

    for i in range(currentColor - 1, -1, -1): # TODO: ici jai change, c'etait : range(currentColor - 1, 0, -1):
        newColoration[vertice] = i
        nbOfConflict = getNumberOfConflict(graph, copy.deepcopy(newColoration))
        if(nbOfConflict <= minNumberOfConflicts):
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
    newColorationWithoutConflict = coloration
    candidateColorationPossiblyConflicted = colorReduction(graph, coloration)
    
    #tabou search
    bestColoration = copy.deepcopy(candidateColorationPossiblyConflicted)
    print('le nombre de conflit initial de la meilleur coloration: ', getNumberOfConflict(graph, bestColoration))

    tabouList = []
    currentColoration = copy.deepcopy(candidateColorationPossiblyConflicted)
    
    
    #BOUCLE
    counter = 0
    while counter < 100:
        #generation de voisins
            #generer nouvelles colorations a partir de la coloration courante
        generatedNeighbours = []
        for vertice in currentColoration.keys():
            for color in range(max(currentColoration.values())):
                if len(tabouList) > 0:
                    trunkatedTabouList = [x[0] for x in tabouList]
                else:
                    trunkatedTabouList = []
                if currentColoration[vertice] != color and (vertice, color) not in trunkatedTabouList:
                    newColoration = copy.deepcopy(currentColoration)
                    newColoration[vertice] = color
                    generatedNeighbours.append((newColoration, (vertice, color)))
        
        #findBest neighbour (min conflicting)
        bestIndex = 0
        minNumberOfConflict = float('inf')
        for idx, neighbour in enumerate(generatedNeighbours):
            nbOfConflicts = getNumberOfConflict(graph, neighbour[0])
            if nbOfConflicts < minNumberOfConflict:
                bestIndex = idx
                minNumberOfConflict = nbOfConflicts
        bestNeighbour = generatedNeighbours[bestIndex][0]
        currentColoration = bestNeighbour
        tupleVerticeColorOfReference = generatedNeighbours[bestIndex][1]
        
        # ajout de couple de reference a la list tabou de la forme ((vertice, color), time)
        tabouList.append([(tupleVerticeColorOfReference), 2*minNumberOfConflict + randrange(1,10)])
        
        if minNumberOfConflict < getNumberOfConflict(graph, bestColoration):
            bestColoration = currentColoration
            counter = 0
            print('le nombre de conflit a bel et bien ete reduit: ', getNumberOfConflict(graph, bestColoration))
        
        if getNumberOfConflict(graph, bestColoration) == 0:
            #alors tenter de reduire a nouveau le nb de couleurs
            newColorationWithoutConflict = copy.deepcopy(bestColoration)
            print(getNumberOfConflict(graph, bestColoration))
            print('il faudra reduire le nombre de couleur')
            print('nb couleurs avant : ', Helper.findNbOfUniqueColorsInSolution(newColorationWithoutConflict))
            candidateColorationPossiblyConflicted = colorReduction(graph, bestColoration)
            bestColoration = colorReduction(graph, bestColoration)
            print('nb couleurs apres: ', Helper.findNbOfUniqueColorsInSolution(candidateColorationPossiblyConflicted))
            print('nb conflit', getNumberOfConflict(graph, candidateColorationPossiblyConflicted))
            time.sleep(3)
            currentColoration = candidateColorationPossiblyConflicted
            tabouList = []
        
        #update tabou list
        for item in tabouList:
            item[1] -= 1
        tabouList[:] = [x for x in tabouList if x[1] > 0]
        
        counter += 1
    
    return newColorationWithoutConflict

def updateTabouList(tabouList, counter): 
    tabouList = [x for x in tabouList if x[1] > counter]
    
# def tabouSearch(graph, coloration): 
#     bestColoration = coloration
#     currentColoration = coloration
#     #print('Coloration color init:')
#     #printOrderedDict(currentColoration)
#     tabouList = []
#     nbOfIterations = 1
#     nbConflictBest = getNumberOfConflict(graph, bestColoration)

#     while nbConflictBest > 0 and nbOfIterations < 100: #TODO: Check if is the good number of iterations (analyse)
#         for vertice in currentColoration.keys():
#             initialColor = currentColoration[vertice]
#             #print('Coloration before neighbour generation for node :', vertice)
#             #printOrderedDict(currentColoration)
#             currentColoration = getBestNeighbour(graph, vertice, copy.deepcopy(currentColoration), tabouList) #Génération voisins et choix
#             #print('Coloration after neighbour generation for node :', vertice)
#             #printOrderedDict(currentColoration)
#             nbConflictCurrent = getNumberOfConflict(graph, copy.deepcopy(currentColoration))
#             nbConflictBest = getNumberOfConflict(graph, copy.deepcopy(bestColoration))
#             #print('nb conflict new :', nbConflictCurrent)
#             #print('nb conflict best :', nbConflictBest)

#             timeInTabouList = 2*nbConflictCurrent + randrange(1,10)
#             coupleAlreadyInTabou = False
#             for couple in tabouList:
#                 if couple[0] == vertice:
#                     if couple[1] == initialColor:
#                         coupleAlreadyInTabou = True
#             if not coupleAlreadyInTabou:
#                 tabouList.append([vertice, initialColor, timeInTabouList]) #Ajout a la liste tabou
#             #print('tabou list :', tabouList)


#             if nbConflictCurrent < nbConflictBest: 
#                 bestColoration = copy.deepcopy(currentColoration) #Comparaison avec la meilleure coloration
#         for couple in tabouList:
#             couple[2] -= 1 #Decremente le temps dans la liste tabou
#             if (couple[2] == 0):
#                 #print('remove in tabou;', couple)
#                 tabouList.remove(couple)
#         #print(tabouList)

#         nbOfIterations += 1
#         #print('nb iteration: ', nbOfIterations)
#     return bestColoration

# def getBestNeighbour(graph, vertice, coloration, tabouList):
#     numberOfColorsAvailable = max(coloration.values()) + 1
#     colorsInTabouList = []
#     for couple in tabouList:
#         if (couple[0] == vertice):
#             colorsInTabouList.append(couple[1])
#     minNumberOfConflicts = float('inf')
#     newColoration = copy.deepcopy(coloration)

#     for i in range(numberOfColorsAvailable - 1, -1, -1): # TODO: ici change 0 a -1
#         if(i != coloration[vertice] and i not in colorsInTabouList):
#             newColoration[vertice] = i
#             nbOfConflict = getNumberOfConflict(graph, copy.deepcopy(newColoration))
#             if(nbOfConflict < minNumberOfConflicts):
#                 minNumberOfConflicts = nbOfConflict
#     #printOrderedDict(newColoration)
#     return newColoration

def printOrderedDict(result):
    sortedResult = dict(sorted(result.items()))
    # for val in sortedResult.values() :
    #     print(val, end=" ")
    print(sortedResult)
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
    
    colorationTabou = tabou2(graph1)
    print('Result tabou : ')
    printOrderedDict(colorationTabou)
    print(Helper.findNbOfUniqueColorsInSolution(colorationTabou))
    
    
    # colorationTabou = tabou(graph1)
    # print('Result tabou : ')
    # printOrderedDict(colorationTabou)
    # print(Helper.findNbOfUniqueColorsInSolution(colorationTabou))