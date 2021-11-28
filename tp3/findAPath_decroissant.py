import copy
graph = { 1 : [2, 3],
          2 : [4, 7, 1],
          3 : [5, 6, 1],
          4 : [2],
          5 : [7, 3, 8],
          6 : [7, 3],
          7 : [2, 5, 6],
          8: [5]}

graph2 = { 
        1 : [3, 4, 8],
        2 : [5, 6, 7, 10],
        3 : [1, 5, 10],
        4 : [1, 6, 10],
        5 : [2, 3],
        6 : [2, 4],
        7 : [2, 9, 10],
        8 : [1, 10],
        9 : [7],
        10: [2, 3, 4, 7 , 8]
        }

# Pire cas
graph3 = { 
        1 : [10],
        2 : [3],
        3 : [2, 4],
        4 : [3, 5],
        5 : [4, 6],
        6 : [5, 7],
        7 : [6, 8],
        8 : [7, 9],
        9 : [8, 10],
        10: [1, 9]
        }

# taille 15 random, mais interessant
# meilleure solution trouvee manuellement : 2, 7, 6, 5, 8, 9, 1, 3, 4, 11, 10, 12, 13, 14, 15 avec 6 conflits
# encore meilleure solution trouvee par prog [5, 6, 7, 2, 8, 9, 1, 3, 4, 11, 10, 12, 13, 14, 15] avec 5 conflits
graph4 = {
    1: [3, 4, 9, 15],
    2: [7, 8, 10, 13],
    3: [1, 4, 8],
    4: [1, 3, 11],
    5: [6, 8, 9],
    6: [5, 7],
    7: [2, 6],
    8: [2, 3, 5, 9],
    9: [1, 5, 8],
    10: [2, 11, 12],
    11: [4, 10],
    12: [10, 13],
    13: [2, 12, 14],
    14: [13, 15],
    15: [1, 14],
}


def findAPath_decroissant(graph):
    totalNbOfStudents = len(graph)
    decreasingOrderedStudent = sorted(list(graph.keys()), reverse=True) #TODO: Quand on va utiliser les vrais instances il faudra trier par ordre de grandeur (pas necessairement le numero de letudiant)
    solution = ([], float('inf'))
    
    for startingNode in decreasingOrderedStudent:
        node_pile = []
        path = [] 
        tabouList = {}
        for student in decreasingOrderedStudent:
            tabouList[student] = set()
            
        path.append(startingNode)
        node_pile.append((startingNode, copy.copy(graph[startingNode]))) 
        
        counter = 0
        while(node_pile):
            counter += 1
            if counter == 10000: # extremement hardcodé, ca fait une difference sur 66_970
                ### TODO: faire qq stats pour le choix de counter
                ## stats counter == 100'000
                # 66_99       nbMin = ERREUR, tempsPris = pas bcp
                # 66_534      nbMin = 40, tempsPris = 1min 6sec
                # 66_970      nbMin = 32, tempsPris = 2min 23sec
                # 118_178     nbMin = ERREUR, tempsPris = 1min 30
                # 118_1570    nbMin = 85, tempsPris = environ 5min
                # 118_2962    nbMin = 58, tempsPris = 9min 30
                # 558_837     nbMin = ERREUR, tempsPris = 19 min
                # 558_31973   nbMin = , tempsPris =
                # 558_63109   nbMin = , tempsPris =
                # 
                ###
                break
                
            while node_pile and not node_pile[-1][1]:
                tabouList[node_pile[-1][0]] = set()
                node_pile.pop()
                path.pop()
                
            if not node_pile:
                break
            
            currentStudent = node_pile[-1][1].pop()
            path.append(currentStudent)
            
            friendsAvailable = []
            hisFriends = graph[currentStudent]
            for friend in hisFriends:
                if friend not in path and friend not in tabouList[currentStudent]:
                    friendsAvailable.append(friend)
            
            friendsAvailable.sort() # les plus grands sont vers la 'droite', donc ils seront pop en premier
            
            if not friendsAvailable:
                ##
                if len(path) == totalNbOfStudents:
                    pathInAscendingOrder = copy.copy(path)
                    pathInAscendingOrder.reverse()
                    nbOfObstructions = findNbOfObstructions(pathInAscendingOrder)
                    
                    if nbOfObstructions < solution[1]:
                        print('======== +!+!+!+!+!+ better solution found +!+!+!+!+!+  ======== conflicts: ', nbOfObstructions)
                        solution = (copy.copy(path), nbOfObstructions)
                
                path.pop()
                tabouList[path[-1]].add(currentStudent)
            else :
                node_pile.append((currentStudent, friendsAvailable))
    
    solution[0].reverse()
    if (solution[0] == []):
        print("NO SOLUTION FOUND !! :(")
    return solution[0]


def findNbOfObstructions(path):
    if not path:
        return -1
    nbOfObstructions = 0
    highestStudent = path[0]
    for student in path:
        if student < highestStudent:
            nbOfObstructions += 1
        elif student > highestStudent:
            highestStudent = student
    return nbOfObstructions


if __name__ == '__main__':
    solution = findAPath_decroissant(graph4)
    nbOfObstructions = findNbOfObstructions(solution)
    print("Last solution found : ", solution)
    print("nb of obstructions: ", nbOfObstructions)