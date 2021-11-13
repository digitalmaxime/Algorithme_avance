import copy

from graph import Helper
from glutton import glutton

def isColorIsConflicting(color, vertice, graph, coloration):
    for neighbour in graph[vertice]: 
        if neighbour in coloration and color == coloration[neighbour]:
            return True
    return False


def explore_node(graph, coloration):
    node_list = []
    vertice = Helper.findMaxSaturatedVertice(graph, coloration)
    for i in range(len(coloration) + 1):
        if not isColorIsConflicting(i, vertice, graph, coloration):
            colorationCopy = copy.deepcopy(coloration)
            colorationCopy[vertice] = i
            node_list.append(colorationCopy)
    return node_list


def checkIfAllVerticesInSolution(solution, graph) :
    for vertice in graph:
        if not vertice in solution:
            return False
    return True


def branch_bound(G) :
    currentBestSolution = glutton(G) # approximation de la meilleure solution via glouton
    UB = Helper.findNbOfUniqueColorsInSolution(currentBestSolution) # upper bound, la valeur qu'on essaie d'ameliorer

    node_pile = []
    coloration = {}
    vertice = Helper.getVerticeWithMaxDegree(G)
    coloration[vertice] = 0
    node_pile.append(coloration) # pile LIFO pour fouille en profondeur
    while node_pile:
        coloration = node_pile.pop()

        if checkIfAllVerticesInSolution(coloration, G):
            nbOfUniqueColorsFound = Helper.findNbOfUniqueColorsInSolution(coloration)
            if nbOfUniqueColorsFound < UB: # si tous les sommets sont dans la coloration, on verifie si le nb de couleurs utilise est meilleur que UB
                UB = nbOfUniqueColorsFound
                currentBestSolution = coloration
                print('b_and_b found a new current Best solution, nb color used: ', Helper.findNbOfUniqueColorsInSolution(currentBestSolution))
        
        elif Helper.findNbOfUniqueColorsInSolution(coloration) < UB:
            node_list = explore_node(G, coloration)
            for new_coloration in node_list:
                node_pile.append(new_coloration) 

    return currentBestSolution
