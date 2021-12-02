import copy


def findAPath_decroissant_w_LB(graph, should_print_solution):
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
        
        counter = 0;
        while(node_pile):
            counter += 1
            if counter == 100000:
                break
                
            while node_pile and not node_pile[-1][1]:
                tabouList[node_pile[-1][0]] = set()
                node_pile.pop()
                path.pop()
                
            if not node_pile:
                break
            
            currentStudent = node_pile[-1][1].pop()
            path.append(currentStudent)
            
            lowerBound = findLowerBound(graph, path)
            if lowerBound and lowerBound >= solution[1]:
                tabouList[path[-1]].add(currentStudent)
                path.pop()
                continue
            
            friendsAvailable = []
            hisFriends = graph[currentStudent]
            for friend in hisFriends:
                if friend not in path and friend not in tabouList[currentStudent]:
                    friendsAvailable.append(friend)
            
            friendsAvailable.sort() # les plus grands sont vers la 'droite', donc ils seront pop en premier
            
            if not friendsAvailable:
                if len(path) == totalNbOfStudents:
                    pathInAscendingOrder = copy.copy(path)
                    pathInAscendingOrder.reverse()
                    nbOfObstructions = findNbOfObstructions(pathInAscendingOrder)
                    if nbOfObstructions < solution[1]:
                        solution = (copy.copy(path), nbOfObstructions)
                        if should_print_solution:
                            tempPath = copy.deepcopy(solution[0])
                            tempPath.reverse()
                            for student in tempPath:
                                print(student, end=" ")
                            print()
                        else:
                            print(nbOfObstructions)
                
                path.pop()
                tabouList[path[-1]].add(currentStudent)
            else :
                node_pile.append((currentStudent, friendsAvailable))
    
    solution[0].reverse()
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
    differenceInLength = len(graph) - len(path)
    if differenceInLength == 0:
        return None
    
    currentNbOfObstructions = 0
    remainingStudents = [x for x in graph.keys() if x not in path]
    remainingStudents.sort(reverse=True)
    highestStudent = remainingStudents[0]
    for student in reversed(path):
        if student < highestStudent:
            currentNbOfObstructions += 1
        elif student > highestStudent:
            highestStudent = student
    return currentNbOfObstructions


if __name__ == '__main__':
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
    solution = findAPath_decroissant_w_LB(graph4, False)
    nbOfObstructions = findNbOfObstructions(solution)
    print("Last solution found : ", solution)
    print("nb of obstructions: ", nbOfObstructions)