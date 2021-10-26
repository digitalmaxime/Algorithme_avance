from graph import Helper
from graph import Helper
from glutton import glutton

G = { 
#    "a" : ["b","c"],
#    "b" : ["a", "d"],
#    "c" : ["a", "d"],
   "d" : ["b", "c", "e"],
   "e" : ["d"]
}

C = {
    "a": 0,
    "b": 1,
    "c": 1,
    "d": 0,
    "e": 1
}

# def explore_node(coloration, G):


def findNbOfUniqueColorsInSolution(solution):
    listOfColors = []
    for colorNumber in solution.values(): 
        if colorNumber not in listOfColors:
            listOfColors.append(colorNumber)
    return len(listOfColors)

def checkIfAllVerticesInSolution(solution, G) :
    listOfAllVerticesInSolution = []
    for vertice in solution:
        listOfAllVerticesInSolution.append(vertice)
    for vertice in G:
        if not vertice in solution:
            return False
    return True

def branch_and_bound(G) :
    currentBestSolution = glutton(G)
    UB = findNbOfUniqueColorsInSolution(currentBestSolution)
    node_pile = []
    coloration = {}
    vertice = Helper.getVerticeWithMaxDegree(G)
    coloration[vertice] = 0
    node_pile.append(coloration)
    while node_pile:
        coloration = node_pile.pop()
        if checkIfAllVerticesInSolution(coloration, G):
            nbOfUniqueColorsFound = findNbOfUniqueColorsInSolution(coloration)
            if nbOfUniqueColorsFound < UB:
                UB = nbOfUniqueColorsFound
                currentBestSolution = coloration
        # else:
            # node_list = explore_node(coloration)
            # for new_coloration in node_list:
            #     node_pile.append(new_coloration)
    return coloration

if __name__ == "__main__":
    print(branch_and_bound(G))
