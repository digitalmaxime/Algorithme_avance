import copy

from read_file import Build_graph
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
        coloration = node_pile.pop() # disons {noeudA : couleur0}, 

        if checkIfAllVerticesInSolution(coloration, G):
            nbOfUniqueColorsFound = Helper.findNbOfUniqueColorsInSolution(coloration)
            if nbOfUniqueColorsFound < UB: # si tous les sommets sont dans la coloration, on verifie si le nb de couleurs utilise est meilleur que UB
                UB = nbOfUniqueColorsFound
                currentBestSolution = coloration
        
        elif Helper.findNbOfUniqueColorsInSolution(coloration) < UB: # si {A:0} ne comprend pas tous les sommets, ..vrai
            node_list = explore_node(G, coloration) # explore genere {A:0, B:1}
            for new_coloration in node_list:
                node_pile.append(new_coloration) # ajout de {A:0, B:1} sur la pile

    return currentBestSolution
