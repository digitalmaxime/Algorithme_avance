import itertools

G = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
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


class Graph: 
    def __init__(self, G):
        self.G = G
        self.C = {"a": 0}

    def getVerticeWithMaxDegree(self, graph):
        maxVertice = list(graph.keys())[0]
        for vertice in graph: 
            if len(graph[vertice]) > len(graph[maxVertice]): 
                maxVertice = vertice
        return maxVertice

    def getSaturationDegree(self, vertice): 
        satDegree = 0
        edges = self.G[vertice]
        for edge in edges: 
            if edge in self.C.keys():
                satDegree += 1
        return satDegree

    def glouton(self, graph):
        v = self.getVerticeWithMaxDegree(graph)
        coloration = {}
        coloration[v] = 0
        #print("coloration", coloration)
        while len(coloration) < len(graph): # Tant que C ne contient pas tous les sommets
            v = self.findMaxSaturatedVertice(graph, coloration)
            #print("sommet choisi", v)
            neighboursColor = [] #Associer la plus petite couleur possible a ce sommet et mettre a jour C
            for neighbour in graph[v]:
                if neighbour in list(coloration.keys()):
                    neighboursColor.append(coloration[neighbour])
                    #print("couleur de ses voisins", neighboursColor)
            for i in range(len(coloration) + 1):
                if i not in neighboursColor:
                    coloration[v] = i
                    #print("coloration", coloration)
                    break

        return coloration

    def findMaxSaturatedVertice(self, graph, coloration):
        mostSaturatedVertices = []
        maxSatDegree = 0
        for vertice in graph.keys(): #Get max degree of saturation
            if vertice not in coloration.keys():
                satDegree = self.getSaturationDegree(vertice)
                if satDegree > maxSatDegree:
                    maxSatDegree = satDegree
        for vertice in graph.keys(): #Get vertices with that degree
            if vertice not in coloration.keys():
                satDegree = self.getSaturationDegree(vertice)
                if satDegree == maxSatDegree:
                    mostSaturatedVertices.append(vertice)
                    
        if len(mostSaturatedVertices) > 1: #Get THE vertice
            subGraph = {}
            for mostSaturatedVertice in mostSaturatedVertices:
                subGraph[mostSaturatedVertice] = graph[mostSaturatedVertice]
            v = self.getVerticeWithMaxDegree(subGraph)
        else:
            v = mostSaturatedVertices[0]
        return v

    def tabou(self, graph): 
        coloration = self.glouton(graph)
        numberOfColorUsed = max(coloration.values()) + 1
        #Color reduction : 
        for vertice in coloration.keys(): 
            if(coloration[vertice] == numberOfColorUsed - 1):
                #Changer de couleur pour minimiser CD
                print(vertice)
        return coloration

    def getNumberOfConflict(self, graph, coloration): 
        nbOfConflict = 0
        for vertice in graph.keys():
            for neighbour in graph[vertice]: 
                if(coloration[vertice] == coloration[neighbour]):
                    nbOfConflict += 1
        return nbOfConflict / 2

    def branch_bound(self, graph): 





if __name__ == "__main__":
    inst = Graph(G)
    #print(inst.tabou(G))
    print(inst.getNumberOfConflict(G,C))