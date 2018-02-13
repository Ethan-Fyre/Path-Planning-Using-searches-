# project2.py
# Ethan Sayles
# February 6, 2018
#
# Purpose: Create a program that utilizes various searching algorithms to find the optimal solution through a terrain.

import argparse
import numpy as np
import search as aima


class Search(aima.Problem):
    def __init__(self, initial, goal, graph):
        aima.Problem.__init__(self, initial, goal)
        self.graph = graph
    def actions(self, state):
        #State in this case is the coords of the current position
        '''If edge piece only actions are away from edge
            if state == [0,0]: actions are d, dr, r
            elif state == [0,height]: actions are u, ur, r
            elif state == [width, 0]: actions are l, dl, d
            elif state == [width, height]: actions are u, ul, l
            elif state[0] == 0: actions are u, ur, r, dr, d
            elif state[0] == width: actions are u, ul, l, dl, d
            elif state[1] == 0: actions are l, dl, d, dr, r
            elif state[1] == height: actions are l, ul, u, ur, r
            else: actions are u, ul , l, dl, d, dr, r, ur'''
        pass

    def result(self, state, action):
        #depending on direction change the value of state to get your output state.
        pass
    def goal_test(self, state):
        #if state == goal, both are of form [x,y]
        pass

    def path_cost(self, c, state1, action, state2):
        #using action check against speed from state1 and state2, to calculate the total time
        #all diagonals are in one if, all hv are in one elif.
        '''if direc == 'dg':
            return np.sqrt(2)/2 * (self.map[self.currrow][self.currcol] + self.map[coord[0]][coord[1]])
        '''
        pass
def main():
    parser = argparse.ArgumentParser(description='Plan a route through a grid.')
    parser.add_argument("grid", help="map/grid filename (a CSV file")
    parser.add_argument("start", help="starting location as a pair r,c")
    parser.add_argument("stop", help="ending location as a pair r,c")
    parser.add_argument("--alg", default='A_star', help="algorithm to use to search (default: A_star)")
    parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")

    args = parser.parse_args()
