#!/usr/bin/env python3

import argparse
import os

from check_sol import load_instance
from build_graph import Build_graph
from findAPath_decroissant_w_lowerBound import findAPath_decroissant_w_LB


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
        
        singlePath = findAPath_decroissant_w_LB(graphDict,  should_print_solution)

