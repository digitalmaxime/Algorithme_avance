class Helper: 
    def getVerticeWithMaxDegree(graph):
        maxVertice = list(graph.keys())[0]
        for vertice in graph: 
            if len(graph[vertice]) > len(graph[maxVertice]): 
                maxVertice = vertice
        return maxVertice

    def getSaturationDegree(vertice, graph, coloration): 
        satDegree = 0
        edges = graph[vertice]
        for edge in edges: 
            if edge in coloration.keys():
                satDegree += 1
        return satDegree

    def findMaxSaturatedVertice(graph, coloration):
        mostSaturatedVertices = []
        maxSatDegree = 0
        for vertice in graph.keys(): # Get max degree of saturation
            if vertice not in coloration.keys():
                satDegree = Helper.getSaturationDegree(vertice, graph, coloration)
                if satDegree > maxSatDegree:
                    maxSatDegree = satDegree
        for vertice in graph.keys(): # Get vertices with that degree
            if vertice not in coloration.keys():
                satDegree = Helper.getSaturationDegree(vertice, graph, coloration)
                if satDegree == maxSatDegree:
                    mostSaturatedVertices.append(vertice)
                    
        if len(mostSaturatedVertices) > 1: # Get the vertice with max saturated degree
            subGraph = {}
            for mostSaturatedVertice in mostSaturatedVertices:
                subGraph[mostSaturatedVertice] = graph[mostSaturatedVertice]
            v = Helper.getVerticeWithMaxDegree(subGraph)
        else:
            v = mostSaturatedVertices[0]
        return v

    def findNbOfUniqueColorsInSolution(solution):
        listOfColors = []
        for colorNumber in solution.values(): 
            if colorNumber not in listOfColors:
                listOfColors.append(colorNumber)
        return len(listOfColors)
