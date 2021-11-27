import copy
import time 
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
# meilleure solution trouvee manuellement : 2, 7, 6, 5, 8, 9, 1, 3, 4, 11, 10, 12, 13, 14, 15
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


def findAPath(graph):
    totalNbOfStudents = len(graph)
    decreasingOrderedStudent = sorted(list(graph.keys()), reverse=True) #TODO: Quand on va utiliser les vrais instances il faudra trier par ordre de grandeur (pas necessairement le numero de letudiant)
    solution = ([], float('inf'))
    counter = 0
    for startingNode in decreasingOrderedStudent:
        counter += 1
        if counter == 2:
            break
        
        node_pile = []
        tabouList = {} # TODO: faire en sorte que ce soit un dict de val : set (pas de val dupliquees)
        path = [] 
        
        
        for student in decreasingOrderedStudent:
            tabouList[student] = []
        
        print('*' * 60)
        print('ITERATION OF FBIG FOR LOOP, starting node : ', startingNode)
        
        path.append(startingNode)
        node_pile.append((startingNode, copy.copy(graph[startingNode])))    
        print('path: ', path)    
        print('node_pile: ', node_pile)   
        print(tabouList) 
        
        counter2 = 0;
        while(node_pile):
            counter2 += 1
            if counter2 == 1000: # extremement hardcodé
                break
                
            while node_pile and not node_pile[-1][1]:
                tabouList[node_pile[-1][0]] = []
                node_pile.pop()
                path.pop()
                
            #  SINON fuck up desfois    
            if not node_pile:
                print("***************  not node pile : ", node_pile)
                break
            
            currentStudent = node_pile[-1][1].pop()
            # print('-' * 50)
            # print("currentStudent : ", currentStudent)
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
                    print('========= solution found ========= ') # TODO: il trouve plusieurs fois la mm solution... !!
                    print('previous sol: ')
                    print(solution)
                    # path.reverse()
                    nbOfObstructions = findNbOfObstructions(path)
                    print('this path : ')
                    print((path, nbOfObstructions))
                    
                    if nbOfObstructions < solution[1]:
                        print()
                        print('======== +!+!+!+!+!+ better solution found +!+!+!+!+!+  ======== ')
                        # trouver la difference avec la sol precedente
                        # firstDiverginPosition = findFirstDiverginPosition(solution, path)
                        
                        solution = (path, nbOfObstructions)
                        print(solution)
                        print()
                    
                        ## TODO: cette ligne etait une indentation vers la gauche
                        node_pile = []
                        
                        tabouList = {} # TODO: faire en sorte que ce soit un dict de val : set (pas de val dupliquees)
                        path = [] 
                        for student in decreasingOrderedStudent:
                            tabouList[student] = []
                        print('*' * 60)
                        print('INITIALIZATION POST BEST SOLUTION, starting node : ', startingNode)
                        path.append(startingNode)
                        node_pile.append((startingNode, copy.copy(graph[startingNode])))    
                        print('path: ', path)    
                        print('node_pile: ', node_pile)   
                        print(tabouList) 
                        continue
                        ## TODO: cette ligne etait une indentation vers la gauche
                        # break 
                
                path.pop()
                tabouList[path[-1]].append(currentStudent)
                # print()
                # print('BACKTRACK NEEDED, no available friends..and path is not quite ready yet, messed up node: ', currentStudent)

            else :
                node_pile.append((currentStudent, friendsAvailable))
            
            # print()
            # print('===> path so far :  :', path)
            # print('===> node pile after filling with new friends :', node_pile)
            # print('===> tabou list : ', tabouList)
    
    if (solution[0] == []):
        print("NO SOLUTION FOUND !! :(")
    return solution


def findNbOfObstructions(path):
    
    path2 = copy.copy(path) # TODO: soit faire la logique en ordre decroissant, ou refaire tout le programme croissant
    path2.reverse()
    
    if not path2:
        return -1
    nbOfObstructions = 0
    highestStudent = path2[0]
    for student in path2:
        if student < highestStudent:
            nbOfObstructions += 1
        elif student > highestStudent:
            highestStudent = student
    return nbOfObstructions
    

def findFirstDiverginPosition(solution, path):
    counter = 0
    for node in solution[0]:
        if node != path[counter]:
            return counter
        counter += 1        



if __name__ == '__main__':
    test = findFirstDiverginPosition(([15, 14, 13, 12, 10, 11, 4, 3, 8, 2, 7, 6, 5, 9, 1], 8), [15, 14, 13, 12, 9, 8])
    print(test)
    # solution = findAPath(graph4)
    # nbOfObstructions = findNbOfObstructions(solution[0])
    # print("Last solution found : ", solution[0])
    # print("nb of obstructions: ", solution[1])