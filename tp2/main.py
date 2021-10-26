#!/usr/bin/env python3

import argparse
import os
import sys
import numpy as np

# from graph import Graph
from glutton import glutton
from tabou import tabou
from algoBB import branch_and_bound
from read_file import Build_graph

class Params:
    matrix = 0
    time = 1

if __name__ == "__main__":
        
    local_parser = argparse.ArgumentParser()
    local_parser.add_argument("-e1",  "--path", type=str, default="./test_file.txt", help="path to matrix")
    local_parser.add_argument("-a", "--algo", type=str, default="glutton", help="specify which type of algorithm to use : glutton, branch_bound or tabou")
    local_parser.add_argument("-p",   "--print_solution", default=False, action='store_true', help="Boolean that is set to true will print graph coloration")
    local_parser.add_argument("-t",   "--print_execution_time", default=False, action='store_true', help="Boolean that is set to true will print execution time")
    args = local_parser.parse_args()

    path_to_matrix = args.path
    path_exists = os.path.exists(path_to_matrix)
    algo = args.algo

    should_print_solution = args.print_solution
    should_print_time_execution = args.print_execution_time
    
    # Check inputed parameters
    if algo not in ['glutton', 'branch_bound', 'tabou']:
        print('type of algorithm {} is invalid'.format(algo))
        algo = 'glutton'

    if not path_exists:
        print("path to matrix doesnt exists..")

    if path_exists:

        (graphDict, nbVertices) = Build_graph(path_to_matrix)

        # switch case here
        if algo == 'glutton':
            result = glutton(graphDict)
        elif algo == 'branch_bound':
            result = branch_bound(graphDict)
        else:
            result = tabou(graphDict)
        #prepare results file
        with open('results.csv', 'a') as f:
            f.write("{};{};{};\n".format(algo, nbVertices, round(result[Params.time], 4)))


        # show output if user asked for it
        if (should_print_solution):
            print("*" * 40)
            #TODO
            
        if (should_print_time_execution):
            print("*" * 40)
            print("it took {} milliseconds ...".format(result[Params.time]))

