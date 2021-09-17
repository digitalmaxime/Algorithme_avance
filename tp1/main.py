#!/usr/bin/env python3

import argparse
import os
import numpy as np

from algo1 import MultiplyMatrice
from algo1 import GenerateMatrixOfZeros
from read_matrix import Build_matrix

if __name__ == "__main__":
    	
	local_parser = argparse.ArgumentParser()
	local_parser.add_argument("-e1",  "--path1", type=str, default="./test_file.txt")
	local_parser.add_argument("-e2",  "--path2", type=str, default="./test_file.txt")
	local_parser.add_argument("-a", "--algo", type=str, default="conv")
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

	if not path1_exists:
		print("path to matrix 1 doesnt exists..")

	if not path2_exists:
		print("path to matrix 2 doesnt exists..")

	if path1_exists and path2_exists:

		matrix_A = [];
		matrix_B = [];

		Build_matrix(matrix_A, path_to_matrix_1)
		Build_matrix(matrix_B, path_to_matrix_2)
		matrix_A = np.array(matrix_A)
		matrix_B = np.array(matrix_B)

		print(matrix_A)
		print(matrix_B)

		# switch case here
		C = MultiplyMatrice(matrix_A, matrix_B)

		if (should_print_matrix):
			# add '-p' in parameters when calling main.py
			print("*" * 40)
			print(C)
		if (should_print_time_execution):
			print("*" * 40)
			print("it took {} seconds ...".format(13))

			
