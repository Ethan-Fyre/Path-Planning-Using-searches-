# project2.py
# Ethan Sayles
# February 6, 2018
#
# Purpose: Create a program that utilizes various searching algorithms to find the optimal solution through a terrain.

import sys
sys.path.insert(0, './aima-python-master')
import argparse
import numpy as np
import search as aima


class Search(aima.Problem):
    def __init__(self, initial, goal, graph):
        aima.Problem.__init__(self, initial, goal)
        self.graph = graph
        self.width = len(self.graph[0])
        self.height = len(self.graph)

    def actions(self, state):
        """Return the possible directions given the current state."""

        if state == [0,0]:
            return ['d', 'dr', 'r']
        elif state == [0,self.height - 1]:
            return ['u', 'ur', 'r']
        elif state == [self.width - 1 , 0]:
            return ['d', 'dl', 'l']
        elif state == [self.width - 1, self.height - 1]:
            return ['u', 'ul', 'l']
        elif state[0] == 0:
            return ['u', 'ur', 'r', 'dr', 'd']
        elif state[0] == self.width - 1:
            return ['u', 'ul', 'l', 'dl', 'd']
        elif state[1] == 0:
            return ['l', 'dl', 'd', 'dr', 'r']
        elif state[1] == self.height - 1:
            return ['l', 'ul', 'u', 'ur', 'r']
        else:
            return ['u', 'ul', 'l', 'dl', 'd', 'dr', 'r', 'ur']

    def result(self, state, action):
        """depending on direction change the value of state to get your output state."""
        switch = {'u': [0, -1], 'ul': [-1, -1], 'l': [-1, 0], 'dl': [-1, 1],
                  'd': [0, 1], 'dr': [1, 1], 'r': [1, 0], 'ur': [1, -1]}

        return[state[0] + switch[action][0], state[1] + switch[action][1]]

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False


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


searcher = Search([1, 1], [2, 2], [[1, 1, 1], [5, 2, 1], [1, 5, 2]])
print([searcher.result(searcher.initial, i) for i in searcher.actions(searcher.initial)])
print([searcher.goal_test(i)for i in [searcher.result(searcher.initial, i) for i in searcher.actions(searcher.initial)]])
