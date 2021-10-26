from graph import Helper

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


def glutton(graph):
        v = Helper.getVerticeWithMaxDegree(graph)
        coloration = {}
        coloration[v] = 0
        #print("coloration", coloration)
        while len(coloration) < len(graph): # Tant que C ne contient pas tous les sommets
            v = Helper.findMaxSaturatedVertice(graph, coloration)
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

if __name__ == "__main__":
    print(glutton(G))
    # inst = Graph()
    # result = glutton(inst)
    # instWithNumber = Graph(G1)
    #print(inst.getColorWithMinConflict('b', G, C))
    #print(instWithNumber.glutton(G1))
    #print(inst.tabou(G))
    #print(inst.getNumberOfConflict(G,C))