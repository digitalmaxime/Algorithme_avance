from glutton import glutton
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

def tabou(graph): 
        coloration = glutton(graph)
        numberOfColorUsed = max(coloration.values()) + 1
        #Color reduction : 
        for vertice in coloration.keys(): 
            if(coloration[vertice] == numberOfColorUsed - 1):
                coloration[vertice] = Helper.getColorWithMinConflict(vertice, graph, coloration)
        #TODO: Faire la recherche tabou ici
        return coloration

if __name__ == "__main__":
    print(tabou(G))