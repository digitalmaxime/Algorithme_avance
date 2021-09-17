import numpy as np

# a = np.matrix((2,2,2))
# b = np.matrix((1,1,1))
# ret = a - b
# print (ret)

# A = np.array([  [1, 2, 3, 4, 5, 6, 7, 8], 
#                 [1, 2, 3, 4, 5, 6, 7, 8], 
#                 [1, 2, 3, 4, 5, 6, 7, 8], 
#                 [1, 2, 3, 4, 5, 6, 7, 8],
#                 [1, 2, 3, 4, 5, 6, 7, 8],
#                 [1, 2, 3, 4, 5, 6, 7, 8],
#                 [1, 2, 3, 4, 5, 6, 7, 8],
#                 [1, 2, 3, 4, 5, 6, 7, 8]
#                 ])

def GenerateMatrixOfZeros(n):
    C = [[0 for col in range(n)] for row in range(n)]
    return np.array(C)

def MultiplyMatrice(A, B):
    nb_lines = len(A[0])
    C = GenerateMatrixOfZeros(nb_lines)
    for i in range(nb_lines):
        for j in range(nb_lines):
            for k in range(nb_lines):
                C[i][j] += A[i][k] * B[k][j]
    return C


def Strassen(A, B):
    nb_lines = len(A[0])
    C = GenerateMatrixOfZeros(nb_lines)
    if (nb_lines == 1):
        C[0][0] = A[0][0] * B[0][0]
    else: 
        A_11 = A[0 : nb_lines // 2, 0 : nb_lines // 2]
        A_21 = A[nb_lines // 2 : nb_lines, 0 : nb_lines // 2]
        A_12 = A[0 : nb_lines // 2, nb_lines // 2 : nb_lines] 
        A_22 = A[nb_lines // 2 : nb_lines, nb_lines // 2 : nb_lines] 
        
        B_11 = B[0 : nb_lines // 2, 0 : nb_lines // 2]
        B_21 = B[nb_lines // 2 : nb_lines, 0 : nb_lines // 2]
        B_12 = B[0 : nb_lines // 2, nb_lines // 2 : nb_lines] 
        B_22 = B[nb_lines // 2 : nb_lines, nb_lines // 2 : nb_lines] 

        M_1 = Strassen(np.add(A_11, A_22), np.add(B_11, B_22))
        M_2 = Strassen(np.add(A_21, A_22), (B_11))
        M_3 = Strassen(A_11, np.subtract(B_12, B_22))
        M_4 = Strassen(A_22,  np.subtract(B_21, B_11))
        M_5 = Strassen(np.add(A_11, A_12), B_22)
        M_6 = Strassen(np.subtract(A_21, A_11), np.add(B_11, B_12))
        M_7 = Strassen(np.subtract(A_12, A_22), np.add(B_21, B_22))

        C[0 : nb_lines // 2, 0 : nb_lines // 2] = M_1 + M_4 - M_5 + M_7
        C[nb_lines // 2 : nb_lines, 0 : nb_lines // 2] = M_2 + M_4
        C[0 : nb_lines // 2, nb_lines // 2 : nb_lines] = M_3 + M_5
        C[nb_lines // 2 : nb_lines, nb_lines // 2 : nb_lines] = M_1 - M_2 + M_3 + M_6

    return C

def Strassen_threshold(A, B, threshold):
    nb_lines = len(A[0])
    C = GenerateMatrixOfZeros(nb_lines)
    if (nb_lines == threshold):
        C = Mult_Matrice(A, B)
    else: 
        A_11 = A[0 : nb_lines // 2, 0 : nb_lines // 2]
        A_21 = A[nb_lines // 2 : nb_lines, 0 : nb_lines // 2]
        A_12 = A[0 : nb_lines // 2, nb_lines // 2 : nb_lines] 
        A_22 = A[nb_lines // 2 : nb_lines, nb_lines // 2 : nb_lines] 
        
        B_11 = B[0 : nb_lines // 2, 0 : nb_lines // 2]
        B_21 = B[nb_lines // 2 : nb_lines, 0 : nb_lines // 2]
        B_12 = B[0 : nb_lines // 2, nb_lines // 2 : nb_lines] 
        B_22 = B[nb_lines // 2 : nb_lines, nb_lines // 2 : nb_lines] 

        M_1 = Strassen_threshold(np.add(A_11, A_22), np.add(B_11, B_22), threshold)
        M_2 = Strassen_threshold(np.add(A_21, A_22), (B_11), threshold)
        M_3 = Strassen_threshold(A_11, np.subtract(B_12, B_22), threshold)
        M_4 = Strassen_threshold(A_22,  np.subtract(B_21, B_11), threshold)
        M_5 = Strassen_threshold(np.add(A_11, A_12), B_22, threshold)
        M_6 = Strassen_threshold(np.subtract(A_21, A_11), np.add(B_11, B_12), threshold)
        M_7 = Strassen_threshold(np.subtract(A_12, A_22), np.add(B_21, B_22), threshold)

        C[0 : nb_lines // 2, 0 : nb_lines // 2] = M_1 + M_4 - M_5 + M_7
        C[nb_lines // 2 : nb_lines, 0 : nb_lines // 2] = M_2 + M_4
        C[0 : nb_lines // 2, nb_lines // 2 : nb_lines] = M_3 + M_5
        C[nb_lines // 2 : nb_lines, nb_lines // 2 : nb_lines] = M_1 - M_2 + M_3 + M_6

    return C

# print('*' * 40)

# C = Mult_Matrice(A, A)
# print(np.array(C))

# C = Strassen(A, A)
# print(np.array(C))

# C = Strassen_threshold(A, A, 2)
# print(np.array(C))
