import copy
from graph import Helper
from glutton import glutton

G = { 
#    "a" : ["b","c"],
#    "b" : ["a", "d"],
#    "c" : ["a", "d"],
#    "d" : ["b", "c", "e"],
#    "e" : ["d"]
#    "a" : ["b","d", "e"],
#    "b" : ["a", "d", "e"],
#    "c" : [],
#    "d" : ["a", "b", "e"],
#    "e" : ["a", "b", "d"]
   "a" : [],
   "b" : ["c", "e"],
   "c" : ["b"],
   "d" : ["e"],
   "e" : ["d"]
}

C = {
    "a": 0,
    # "b": 1,
    # "c": 1,
    # "d": 0,
    # "e": 1
}

def checkIfColorIsConflicting(color, vertice, graph, coloration):
    for neighbour in graph[vertice]: 
        if neighbour in coloration and color == coloration[neighbour]:
            return True
    return False


def explore_node(graph, coloration):
    node_list = []
    vertice = Helper.findMaxSaturatedVertice(graph, coloration)
    print('max saturated: ', vertice)
    for i in range(len(coloration) + 1):
        print(i)
        if not checkIfColorIsConflicting(i, vertice, graph, coloration):
            colorationCopy = copy.deepcopy(coloration)
            colorationCopy[vertice] = i
            node_list.append(colorationCopy)
    return node_list


def findNbOfUniqueColorsInSolution(solution):
    listOfColors = []
    for colorNumber in solution.values(): 
        if colorNumber not in listOfColors:
            listOfColors.append(colorNumber)
    return len(listOfColors)

def checkIfAllVerticesInSolution(solution, graph) :
    # listOfAllVerticesInSolution = []
    # for vertice in solution:
    #     listOfAllVerticesInSolution.append(vertice)
    print('check if all vertices in sol')
    print('sol: ', solution)
    print('graph: ', graph)
    for vertice in graph:
        if not vertice in solution:
            print('false')
            return False
    print('true')
    return True

def branch_and_bound(G) :
    currentBestSolution = glutton(G)
    UB = findNbOfUniqueColorsInSolution(currentBestSolution)
    print('firt solution : ', currentBestSolution)
    node_pile = []
    coloration = {}
    vertice = Helper.getVerticeWithMaxDegree(G)
    coloration[vertice] = 0
    node_pile.append(coloration)
    while node_pile:
        coloration = node_pile.pop()
        print('findNbOfUniqueColorsInSolution', findNbOfUniqueColorsInSolution(coloration))
        print('UB', UB)
        if checkIfAllVerticesInSolution(coloration, G):
            nbOfUniqueColorsFound = findNbOfUniqueColorsInSolution(coloration)
            if nbOfUniqueColorsFound < UB:
                UB = nbOfUniqueColorsFound
                currentBestSolution = coloration
        elif findNbOfUniqueColorsInSolution(coloration) < UB:
            node_list = explore_node(G, coloration)
            for new_coloration in node_list:
                node_pile.append(new_coloration)
    return currentBestSolution

if __name__ == "__main__":
    print("*" * 40)
    print(branch_and_bound(G))
    # explore_node(G, C)
    
