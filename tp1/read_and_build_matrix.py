def Build_matrix(path):
    matrix = []
    with open(path) as f:
        power_n = f.readline().strip()
        data = f.read()
        listOfLines = data.split('\n')
        for line in listOfLines:
            if line == "\n" or line == "":
                pass
            else:
                parsedLine = line.split(' ')
                for i in range(len(parsedLine)):
                        parsedLine[i] = int(parsedLine[i])
                matrix.append(parsedLine)
    return matrix, power_n