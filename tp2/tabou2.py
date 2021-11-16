from glutton import glutton
from graph import Helper
from random import randrange
import copy
from read_file import Build_graph
from branch_and_bound import branch_bound


def colorReduction(graph, coloration): 
    colorationReduced = copy.copy(coloration)
    maxColorUsed = max(coloration.values())
    
    for vertice in coloration.keys(): 
        if(coloration[vertice] == maxColorUsed):
            color = getColorWithMinConflict(vertice, graph, colorationReduced)  # TODO: ici chage coloration a colorationReduced
            colorationReduced[vertice] = color
    return colorationReduced


def getColorWithMinConflict(vertice, graph, coloration): 
    currentColor = coloration[vertice]
    newColoration = copy.copy(coloration)
    minNumberOfConflicts = float('inf')

    for i in range(currentColor - 1, -1, -1): # TODO: ici jai change, c'etait : range(currentColor - 1, 0, -1):
        newColoration[vertice] = i
        nbOfConflict = getNumberOfConflictOfSpecificVertice(graph, newColoration, vertice)
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

def getNumberOfConflictOfSpecificVertice(graph, coloration, vertice):
    nbOfConflict = 0
    for neighbour in graph[vertice]: 
        if(coloration[vertice] == coloration[neighbour]):
            nbOfConflict += 1
    return nbOfConflict


def tabouSearch(graph, coloration):
    # recherche tabou
    bestColoration = coloration
    currentColoration = bestColoration
    tabouList = []
    
    nbOfIterations = 0
    while nbOfIterations < 2*len(coloration): # TODO: choix de condition while        
        # juste pour faciliter le code python plus tard
        if len(tabouList) > 0:
            trunkatedTabouList = [x[0] for x in tabouList]
        else:
            trunkatedTabouList = []
            
        # generation de voisins
        # i.e generer nouvelles colorations a partir de la coloration courante
        generatedNeighbours = []
        for vertice in currentColoration.keys():
            for color in range(max(currentColoration.values())):
                if currentColoration[vertice] != color and (vertice, color) not in trunkatedTabouList:
                    newColoration = copy.copy(currentColoration)
                    newColoration[vertice] = color
                    generatedNeighbours.append((newColoration, (vertice, color)))
        
        # trouver le meilleur voisin (min conflits)
        bestIndex = 0
        minNumberOfConflict = float('inf')
        for idx, neighbour in enumerate(generatedNeighbours):
            nbOfConflicts = getNumberOfConflict(graph, neighbour[0])
            if nbOfConflicts < minNumberOfConflict:
                bestIndex = idx
                minNumberOfConflict = nbOfConflicts
        
        bestNeighbour = generatedNeighbours[bestIndex][0]
        currentColoration = bestNeighbour
        
        # ajout de couple de reference a la list tabou de la forme ((vertice, color), time)
        tupleVerticeColorOfReference = generatedNeighbours[bestIndex][1]
        tabouList.append([(tupleVerticeColorOfReference), 2*minNumberOfConflict + randrange(1,10)])
        
        # evaluter si la solution trouvee est meilleure que le bestColoration
        nbOfConflictsOfCurrentColoration = getNumberOfConflict(graph, currentColoration)
        nbOfConflictsOfBestColoration = getNumberOfConflict(graph, bestColoration)
        if nbOfConflictsOfCurrentColoration < nbOfConflictsOfBestColoration:
            bestColoration = currentColoration
            nbOfIterations = 0
        
        #update tabou list
        for item in tabouList:
            item[1] -= 1
        tabouList[:] = [x for x in tabouList if x[1] > 0]
        
        nbOfIterations += 1
    
    return bestColoration


def tabou2(graph): 
    bestColorationWithoutConflict = glutton(graph)
    
    #Loop between colorReduction and tabouSearch until tabouSearch fails
    while (True): 
        newColorationWithConflict = colorReduction(graph, bestColorationWithoutConflict)
        resultTabou = tabouSearch(graph, newColorationWithConflict)
        
        numberOfConflictTabou = getNumberOfConflict(graph, resultTabou)
        if (numberOfConflictTabou > 0): 
            break
        else: 
            bestColorationWithoutConflict = copy.copy(resultTabou)
    return bestColorationWithoutConflict
    

if __name__ == "__main__":
    
    (graph1, num) = Build_graph("./generated_files/gen_ex30_2")
    
    colorationGlutton = glutton(graph1)
    print('Result glouton : ')
    print(Helper.findNbOfUniqueColorsInSolution(colorationGlutton))
    print("-" * 60)
    colorationBranch = branch_bound(graph1)
    print('Result branch : ')
    print(Helper.findNbOfUniqueColorsInSolution(colorationBranch))
    print("-" * 60)
    
    colorationTabou = tabou2(graph1)
    print('Result tabou : ')
    print(Helper.findNbOfUniqueColorsInSolution(colorationTabou))
    print("-" * 60)
    
