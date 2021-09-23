#!/usr/bin/env python3

import argparse
import os
import sys
import numpy as np

from algo1 import GenerateMatrixOfZeros
from algo1 import MultiplyMatriceWrapper
from algo1 import StrassenWrapper
from algo1 import StrassenThresholdWrapper
from read_and_build_matrix import Build_matrix

class Params:
    matrix = 0
    time = 1

if __name__ == "__main__":
        
    local_parser = argparse.ArgumentParser()
    local_parser.add_argument("-e1",  "--path1", type=str, default="./test_file.txt", help="path to first matrix")
    local_parser.add_argument("-e2",  "--path2", type=str, default="./test_file.txt", help="path to second matrix")
    local_parser.add_argument("-a", "--algo", type=str, default="conv", help="specify which type of algorithm to use : conv, strassen or strassenSeuil")
    local_parser.add_argument("-p",   "--print_matrix", default=False, action='store_true', help="Boolean that is set to true will print result matrix")
    local_parser.add_argument("-t",   "--print_execution_time", default=False, action='store_true', help="Boolean that is set to true will print execution time")
    args = local_parser.parse_args()

    path_to_matrix_1 = args.path1
    path1_exists = os.path.exists(path_to_matrix_1)
    path_to_matrix_2 = args.path2
    path2_exists = os.path.exists(path_to_matrix_2)
    algo = args.algo

    should_print_matrix = args.print_matrix
    should_print_time_execution = args.print_execution_time
    
    # Check inputed parameters
    if algo not in ['conv', 'strassen', 'strassenSeuil']:
        print('type of algorithm {} is invalid'.format(algo))
        algo = 'conv'

    if not path1_exists:
        print("path to matrix 1 doesnt exists..")

    if not path2_exists:
        print("path to matrix 2 doesnt exists..")

    if path1_exists and path2_exists:

        (matrix_A, power_n) = Build_matrix(path_to_matrix_1)
        (matrix_B, power_n) = Build_matrix(path_to_matrix_2)
        matrix_A = np.array(matrix_A)
        matrix_B = np.array(matrix_B)

        # switch case here
        if algo == 'conv':
            result = MultiplyMatriceWrapper(matrix_A, matrix_B)
        elif algo == 'strassen':
            result = StrassenWrapper(matrix_A, matrix_B)
        else:
            result = StrassenThresholdWrapper(matrix_A, matrix_B, 2) # TODO ici le seuil est hardcode**
        #prepare results file
        with open('results.csv', 'a') as f:
            f.write("{};{};{};\n".format(algo, power_n, round(result[Params.time], 4)))


        # show output if user asked for it
        if (should_print_matrix):
            print("*" * 40)
            print(result[Params.matrix])
            
        if (should_print_time_execution):
            print("*" * 40)
            print("it took {} milliseconds ...".format(result[Params.time]))

