def Build_graph(instance_data):
    numberOfVertices = len(instance_data[0])
    couples = instance_data[1]
    graph = {}

    for i in range(1, numberOfVertices + 1):
        graph[i] = []

    for couple in couples: 
        graph[couple[0]].append(couple[1])
        graph[couple[1]].append(couple[0])
      
    return (graph, numberOfVertices)

if __name__ == "__main__":
    #For testing, ex5_0 is used
    # graph = Build_graph("./instances/ex5_0")
    (graph, numberOfVertices) = Build_graph("./instances/ex5_0")
    print(graph)