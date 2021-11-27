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


def findAPath(graph):
    totalNbOfStudents = len(graph)
    increasingOrderedStudent = sorted(list(graph.keys())) #TODO: Quand on va utiliser les vrais instances il faudra trier par ordre de grandeur (pas necessairement le numero de letudiant)
    solution = ([], float('inf'))
    
    c = 0
    for startingNode in increasingOrderedStudent:
        c += 1
        # if c < 5:
        #     continue
        # if c > 5:
        #     break
        if c == 6:
            break
        node_pile = []
        path = [] 
        tabouList = {} # TODO: faire en sorte que ce soit un dict de val : set (pas de val dupliquees)
        for student in increasingOrderedStudent:
            tabouList[student] = []
        
        # print('*' * 60)
        # print('ITERATION OF FBIG FOR LOOP, starting node : ', startingNode)
        
        path.append(startingNode)
        candidateFriends = sorted(copy.copy(graph[startingNode]), reverse=True)
        
        node_pile.append((startingNode, candidateFriends))    
        # print('path: ', path)    
        # print('node_pile: ', node_pile)   
        # print(tabouList) 
        print(node_pile)
        
        counter = 0;
        while(node_pile):
            counter += 1
            if counter == 10000: # extremement hardcodé, ca fait une difference
                ###
                ## stats counter == 100'000
                # 66_99       nbMin = 
                # 66_534      nbMin = 
                # 66_970      nbMin = 
                # 118_178     nbMin = 
                # 118_1570    nbMin = 
                # 118_2962    nbMin = 
                # 558_837     nbMin = 
                # 558_31973   nbMin = 
                # 558_63109   nbMin = 
                # 
                ###
                break
                
            while node_pile and not node_pile[-1][1]:
                tabouList[node_pile[-1][0]] = []
                node_pile.pop()
                path.pop()
                
            #  SINON fuck up desfois a la fin lorsque tout est fini et il reste genre [(15: []), (14: []), (10: [])]    
            if not node_pile:
                # print("***************  not node pile : ", node_pile)
                break
            
            currentStudent = node_pile[-1][1].pop()
            # print('-' * 50)
            # print("currentStudent : ", currentStudent)
            path.append(currentStudent)
            # lowerBound = findLowerBound(graph, path)
            # if lowerBound and lowerBound >= solution[1]:
            #     print("LOWER BOUND NOT EVEN BETTER, SO MOVING ON")
            #     path.pop()
            #     continue
            
            friendsAvailable = []
            hisFriends = graph[currentStudent]
            for friend in hisFriends:
                if friend not in path and friend not in tabouList[currentStudent]:
                    friendsAvailable.append(friend)
            
            friendsAvailable.sort(reverse=True) # les plus petits sont vers la 'droite', donc ils seront pop en premier
            
            if not friendsAvailable:
                ##
                if len(path) == totalNbOfStudents:
                    print('SOLUTION FOUND______________')
                    print(path)
                    # pathInAscendingOrder = copy.copy(path)
                    # pathInAscendingOrder.reverse()
                    # nbOfObstructions = findNbOfObstructions(pathInAscendingOrder)
                    nbOfObstructions = findNbOfObstructions(path)
                    
                    if nbOfObstructions < solution[1]:
                        print()
                        print('======== +!+!+!+!+!+ better solution found +!+!+!+!+!+  ======== conflicts: ', nbOfObstructions)
                        
                        solution = (copy.copy(path), nbOfObstructions)
                        print(solution)
                
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
    
    # print(solution) 
    # print(solution)
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
    
def findLowerBound(graph, path):
    if not path:
        return -1
    differenceInLength = len(graph) - len(path)
    
    if differenceInLength == 0:
        return None
    
    curretnNbOfObstructions = 0
    highestStudent = path[0]
    for student in path:
        if student < highestStudent:
            curretnNbOfObstructions += 1
        elif student > highestStudent:
            highestStudent = student
            
    remainingStudents = [x for x in graph.keys() if x not in path]
    for student in remainingStudents:
        if student < highestStudent:
            curretnNbOfObstructions += 1
    return curretnNbOfObstructions

# def findFirstDiverginPosition(solution, path):
#     counter = 0
#     for node in solution[0]:
#         if node != path[counter]:
#             return counter
#         counter += 1        



if __name__ == '__main__':
    # node_pile = [(15, [1]), (14, []), (13, [2]), (12, []), (10, []), (11, []), (4, []), (3, []), (8, [])]
    # solution = ([15, 14, 13, 12, 10, 11, 4, 3, 8], 8)
    # test = findFirstDiverginPosition(solution, [15, 14, 13, 12, 10, 11, 4, 3, 1])
    # print(test)
    # node_pile= node_pile[:test]
    # print(node_pile)
    
    solution = findAPath(graph4)
    nbOfObstructions = findNbOfObstructions(solution)
    print("Last solution found : ", solution)
    print("nb of obstructions: ", nbOfObstructions)