def Build_graph(instance_data):
    heightDict = {}
    numberOfVertices = len(instance_data[0])

    #Order by student height
    for i in range(1, numberOfVertices + 1):
        heightDict[i] = instance_data[0][i-1]
    sorted_height = sorted(heightDict.items(), key=lambda kv: kv[1])

    couples = instance_data[1]
    graph = {}

    #Build graph by student height
    for student in sorted_height:
        graph[student[0]] = []

    #Add each student's friends to graph
    for couple in couples: 
        graph[couple[0]].append(couple[1])
        graph[couple[1]].append(couple[0])
      
    return (graph, numberOfVertices)
