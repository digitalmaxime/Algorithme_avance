from convert_to_instances import convert_instance

def Build_graph(path):
    fileName = path.split('/')[-1]
    instance_path = './instances/' + fileName
    convert_instance(path, instance_path)
    graph = {}
    with open(instance_path) as f:
    # with open(path) as f:
        numberOfVertices = f.readline().strip()
        for vertice in range(int(numberOfVertices)):
            graph[vertice] = []
        data = f.read()
        listOfLines = data.split('\n')
        lineNumber = 0
        for line in listOfLines:
            if line == "\n" or line == "":
                pass
            else:
                parsedLine = line.split(' ')
                for i in range(len(parsedLine) - 1):
                    if(int(parsedLine[i]) == 1):
                        graph[lineNumber].append(i)
            lineNumber += 1            
    return (graph, numberOfVertices)

if __name__ == "__main__":
    #For testing, ex5_0 is used
    # graph = Build_graph("./instances/ex5_0")
    (graph, numberOfVertices) = Build_graph("./instances/ex5_0")
    print(graph)