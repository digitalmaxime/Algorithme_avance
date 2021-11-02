from graph import Helper

def glutton(graph):
    v = Helper.getVerticeWithMaxDegree(graph)
    coloration = {}
    coloration[v] = 0

    while len(coloration) < len(graph): # Tant que la coloration ne contient pas tous les sommets
        v = Helper.findMaxSaturatedVertice(graph, coloration)
        neighboursColor = [] # liste des voisins de 'v' qui sont deja colores ('v' devra alors prendre une couleur n'appartenant pas a ses voisins)
        for neighbour in graph[v]: # pour chaque voisin du graph
            if neighbour in list(coloration.keys()):
                neighboursColor.append(coloration[neighbour])
        for i in range(len(coloration) + 1):
            if i not in neighboursColor: # trouver la plus petite couleur n'appartenant pas a ses voisins
                coloration[v] = i
                break

    return coloration
