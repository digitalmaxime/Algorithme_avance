G = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["b", "c", "e"],
   "e" : ["d"]
}

G1 = {0: [3], 1: [2, 3, 4], 2: [1, 3], 3: [0, 1, 2], 4: [1]}

C = {
    "a": 0,
    "b": 2,
    "c": 1,
    "d": 0,
    "e": 1
}


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
        for vertice in graph.keys(): #Get max degree of saturation
            if vertice not in coloration.keys():
                satDegree = Helper.getSaturationDegree(vertice, graph, coloration)
                if satDegree > maxSatDegree:
                    maxSatDegree = satDegree
        for vertice in graph.keys(): #Get vertices with that degree
            if vertice not in coloration.keys():
                satDegree = Helper.getSaturationDegree(vertice, graph, coloration)
                if satDegree == maxSatDegree:
                    mostSaturatedVertices.append(vertice)
                    
        if len(mostSaturatedVertices) > 1: #Get THE vertice
            subGraph = {}
            for mostSaturatedVertice in mostSaturatedVertices:
                subGraph[mostSaturatedVertice] = graph[mostSaturatedVertice]
            v = Helper.getVerticeWithMaxDegree(subGraph)
        else:
            v = mostSaturatedVertices[0]
        return v



if __name__ == "__main__":
    pass
    # inst = Graph()
    # instWithNumber = Graph(G1)
    #print(instWithNumber.glutton(G1))
    #print(inst.tabou(G))
    #print(inst.getNumberOfConflict(G,C))