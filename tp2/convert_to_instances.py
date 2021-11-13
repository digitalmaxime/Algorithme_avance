def convert_instance(sourceFilePath, newFileName):
    matrix = convert_to_matrix(sourceFilePath)
    write_matrix_to_file(matrix, newFileName)

def convert_to_matrix(filePath):
    with open(filePath) as f:
        for line in f.readlines():
            line = line.split(' ');
            if line[0] == 'p':
                numberOfVertices = int(line[2])
                matrix = buildMatrixOfZeros(numberOfVertices)
                               
            elif line[0] == 'e':
                if (line[1] > line[2]):
                    max = int(line[1])
                    min = int(line[2])
                else :
                    min = int(line[1])
                    max = int(line[2])
                matrix[max-1][min-1] = 1
                matrix[min-1][max-1] = 1
    return matrix

def write_matrix_to_file(matrix, newFileName): 
    with open(newFileName, 'w') as f:
        f.write('{}\n'.format(str(len(matrix))))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                f.write('{} '.format(str(matrix[i][j])))
            f.write('\n')
            
def buildMatrixOfZeros(n): 
    matrix = []
    for i in range(n):
        line1byN = []
        for j in range(n):
            line1byN.append(0)
        matrix.append(line1byN)
    return matrix 

if __name__ == "__main__":
    # m = buildMatrixOfZeros(5)
    # print(m)
    #For testing, ex5_0 is used
    for size in [20, 25, 30, 35, 40, 45, 50]:
        for ex in [0, 1, 2, 3, 4]:
            convert_instance("./generated_files/gen_ex{}_{}".format(size, ex), './instances/ex{}_{}'.format(size, ex))
    # print(graph)