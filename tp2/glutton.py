from graph import Helper

def glutton(graph):
    v = Helper.getVerticeWithMaxDegree(graph)
    coloration = {}
    coloration[v] = 0

    while len(coloration) < len(graph): 
        v = Helper.findMaxSaturatedVertice(graph, coloration)
        neighboursColor = [] 
        for neighbour in graph[v]: 
            if neighbour in list(coloration.keys()):
                neighboursColor.append(coloration[neighbour])
        for i in range(len(coloration) + 1):
            if i not in neighboursColor:
                coloration[v] = i
                break

    return coloration
