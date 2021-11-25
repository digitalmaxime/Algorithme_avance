#!/usr/bin/env python3

import argparse
import os
import sys
import time

from check_sol import load_instance
from build_graph import Build_graph
from algo_graph import findAllPaths
from max import findAPath

if __name__ == "__main__":
        
    local_parser = argparse.ArgumentParser()
    local_parser.add_argument("-e",  "--path", type=str, help="path to testset")
    local_parser.add_argument("-p",   "--print_solution", default=False, action='store_true', help="Boolean that is set to true will print rank order")
    args = local_parser.parse_args()

    path_to_testset = args.path
    path_exists = os.path.exists(path_to_testset)

    should_print_solution = args.print_solution
    
    # Check inputed parameters
    if not path_exists:
        print("path to testset doesnt exists..")

    if path_exists:
        instance_data = None
        instance_data = load_instance(path_to_testset)

        (graphDict, nbVertices) = Build_graph(instance_data)
        # print(graphDict)

        singlePath = findAPath(graphDict)
        print("solution found: ", singlePath[0])
        
        #allPaths = []
        #for vertice in graphDict: 
            #result = sorted(findAllPaths(graphDict, vertice))
            #for path in result:
                #allPaths.append(path)

        #print(allPaths)

        # show output if user asked for it
        if (should_print_solution):
            #TODO: print solution in good format
            print()

