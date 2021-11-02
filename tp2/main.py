#!/usr/bin/env python3

import argparse
import os
import sys
import numpy as np
import time


from graph import Helper
from glutton import glutton
from tabou import tabou
from branch_and_bound import branch_bound
from read_file import Build_graph

class Params:
    coloration = 0
    time = 1

if __name__ == "__main__":
        
    local_parser = argparse.ArgumentParser()
    local_parser.add_argument("-e",  "--path", type=str, default="./test_file.txt", help="path to testset")
    local_parser.add_argument("-a", "--algo", type=str, default="glouton", help="specify which type of algorithm to use : glouton, branch_bound or tabou")
    local_parser.add_argument("-p",   "--print_solution", default=False, action='store_true', help="Boolean that is set to true will print graph coloration")
    local_parser.add_argument("-t",   "--print_execution_time", default=False, action='store_true', help="Boolean that is set to true will print execution time")
    args = local_parser.parse_args()

    path_to_testset = args.path
    path_exists = os.path.exists(path_to_testset)
    algo = args.algo

    should_print_solution = args.print_solution
    should_print_time_execution = args.print_execution_time
    
    # Check inputed parameters
    if algo not in ['glouton', 'branch_bound', 'tabou']:
        print('type of algorithm {} is invalid'.format(algo))
        algo = 'glutton'

    if not path_exists:
        print("path to testset doesnt exists..")

    if path_exists:

        (graphDict, nbVertices) = Build_graph(path_to_testset)

        # switch case here
        initial_time = time.perf_counter()
        if algo == 'glouton':
            coloration = glutton(graphDict)
        elif algo == 'branch_bound':
            coloration = branch_bound(graphDict)
        else:
            coloration = tabou(graphDict)
        execution_time = (time.perf_counter() - initial_time)*1000
        result = tuple((coloration, execution_time))
            
        #prepare results file
        with open('results_{}.csv'.format(algo), 'a') as f:
            f.write("{};{};{};\n".format(algo, nbVertices, round(result[Params.time], 4)))

        # show output if user asked for it
        if (should_print_solution):
            print("*" * 40)
            print(Helper.findNbOfUniqueColorsInSolution(result[Params.coloration]))
            sortedResult = dict(sorted(result[Params.coloration].items()))
            for val in sortedResult.values() :
                print(val, end=" ");
            print()
            print("*" * 40)
            
        if (should_print_time_execution):
            print("*" * 40)
            print("it took {} milliseconds ...".format(result[Params.time]))

