import copy
import time 
graph = { 0 : [1, 2],
          1 : [3, 6, 0],
          2 : [4, 5, 0],
          3 : [1],
          4 : [6, 2, 7],
          5 : [6, 2],
          6 : [1, 4, 5],
          7: [4]}

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

def findAPath(graph):
    # sort graph by student height
    #...
    path = []
    tabouList = []
    sortedGraph = graph;
    
    nbOfStudents = len(graph)
    print(nbOfStudents)
    
    #create LIFO of friends
    node_pile = []
    
    highestStudent = findHighestStudent(graph)
    startingNode = copy.copy(highestStudent)
    node_pile.append(highestStudent)
    # tabouList.append(highestStudent)
    
    counter = 0
    while(node_pile):
        lastPlacedStudentInLine = node_pile.pop()
        print('lastPlacedStudentInLine', lastPlacedStudentInLine)
        # case where element (friend) in LIFO doesnt belong to path[-1], perhaps its a friend of path[-2]..
        # while path and lastPlacedStudentInLine not in graph[path[0]]:
        #     print('path[0]', path[0])
        #     print('graph[path[0]', graph[path[0]])
        #     tabouList.append(path[0])
        #     path.pop()
        #     print('updated path', path)
        #     time.sleep(2)
            
        path.append(lastPlacedStudentInLine)
        
        # find lastPlacedStudentInLine list of friends
        friends = []
        hisFriends = graph[lastPlacedStudentInLine]
        for friend in hisFriends:
            if friend not in path and friend not in tabouList:
                friends.append(friend)

        friends.sort() # les plus grands sont vers la 'droite', donc ils seront pop en premier
        if not friends:
            if len(path) == nbOfStudents:
                print('found solution! ? ! ', lastPlacedStudentInLine)
                break
            else :
                tabouList.append(lastPlacedStudentInLine)
                # solution no good, backtrack one step
                path.pop()
                print(' BACKTRACK NEEDED , no friends..and path is not quite ready yet, messed up node: ', lastPlacedStudentInLine)
                if not path:
                    print('epuise toute les ressources, il faut commencer du debut avec un nouveau noeud! ...')
                    break
                    
        else :
            for friend in friends:
                node_pile.append(friend)
        
        print('node pile after filling with new friends :', node_pile)
        # path.reverse()        
        print('path so far :  :', path)
        counter += 1
        if counter == 11:
            break
        
    path.reverse()        
    print("path", path)
    return path
    

def findHighestStudent(graph):
    currentHighestStudent = next(iter(graph))
    for key in graph.keys():
        if key > currentHighestStudent:
            currentHighestStudent = key
    # ou encore
    test = list(graph.keys())[-1]
    # print('currentHighestStudent', currentHighestStudent)
    # print('test', test)
    return currentHighestStudent

def findTallestFriend(student, graph):
    studentFriends = graph[student]
    print('studentFriends', studentFriends)
    print('student', student)
    assert len(studentFriends) > 0, 'studentFriends is empty, oh no!'
    tallestFriend = max(studentFriends)
    return tallestFriend

def findNbOfObstructions(path):
    nbOfObstructions = 0
    highestStudent = path[0]
    for student in path:
        if student < highestStudent:
            nbOfObstructions += 1
        elif student > highestStudent:
            highestStudent = student
    return nbOfObstructions
    

if __name__ == '__main__':
    path = findAPath(graph2)
    # nbOfObstructions = findNbOfObstructions(path2)
    # print(nbOfObstructions)