# project2.py
# Ethan Sayles
# February 6, 2018
#
# Purpose: Create a program that utilizes various searching algoritms to find the optimal solution through a terrain.

import argparse
import numpy as np

class Search:
    def __init__(self,map, currrow = 0, currcol = 0):
        self.currrow = currrow
        self.currcol = currcol
        self.map = map

    def step_cost(self, direc, coord):
        #direc can be 'dg' (diagonal) or 'hv' (horizontal/vertical)

        if direc == 'dg':
            return np.sqrt(2)/2 * (self.map[self.currrow][self.currcol] + self.map[coord[0]][coord[1]])

def main():
    parser = argparse.ArgumentParser(description='Plan a route through a grid.')
    parser.add_argument("grid", help="map/grid filename (a CSV file")
    parser.add_argument("start", help="starting location as a pair r,c")
    parser.add_argument("stop", help="ending location as a pair r,c")
    parser.add_argument("--alg", default='A_star', help="algorithm to use to search (default: A_star)")
    parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")

    args = parser.parse_args()
