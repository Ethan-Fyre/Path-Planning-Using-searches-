# project2.py
# Ethan Sayles
# February 6, 2018
#
# Purpose: Create a program that utilizes various searching algorithms to find the optimal solution through a terrain.

import argparse
import numpy as np
import search as aima


class Search(aima.Problem):
    def __init__(self, initial, goal, filename):
        aima.Problem.__init__(self, initial, goal)
        self.graph = np.loadtxt(filename, delimiter=',')
        self.width = len(self.graph[0])
        self.height = len(self.graph)

    def actions(self, state):
        """Return the possible directions given the current state."""

        if state == (0, 0):
            return ['d', 'dr', 'r']
        elif state == (0, self.height - 1):
            return ['u', 'ur', 'r']
        elif state == (self.width - 1, 0):
            return ['d', 'dl', 'l']
        elif state == (self.width - 1, self.height - 1):
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
        switch = {'u': (0, -1), 'ul': (-1, -1), 'l': (-1, 0), 'dl': (-1, 1),
                  'd': (0, 1), 'dr': (1, 1), 'r': (1, 0), 'ur': (1, -1)}
        result = [state[0] + switch[action][0], state[1] + switch[action][1]]
        if self.graph[result[1]][result[0]] != 0:
            return tuple(result)
        else:
            return state

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False

    def path_cost(self, c, state1, action, state2):
        if self.graph[state2[1]][state2[0]] == 0 or self.graph[state1[1]][state1[0]] == 0:
            return aima.infinity
        if action in ['d', 'r', 'u', 'l']:
            return c + 1 / 2 * (1 / self.graph[state1[1]][state1[0]] + 1 / self.graph[state2[1]][state2[0]])
        else:
            return c + np.sqrt(2) / 2 * (1 / self.graph[state1[1]][state1[0]] + 1 / self.graph[state2[1]][state2[0]])

    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        return int(aima.distance(node.state, self.goal))

def main():
    searcher = Search(start, stop, args.grid)
    if args.alg == 'bfs':
        search = aima.breadth_first_search(searcher)
    elif args.alg == 'ucs':
        search = aima.uniform_cost_search(searcher)
    else:
        search = aima.astar_search(searcher)
    return search.path()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plan a route through a grid.')
    parser.add_argument("grid", help="map/grid filename (a CSV file")
    parser.add_argument("start", help="starting location as a pair r,c")
    parser.add_argument("stop", help="ending location as a pair r,c")
    parser.add_argument("--alg", default='a_star', help="algorithm to use to search (default: A_star)")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    args = parser.parse_args()
    start = tuple([int(i) for i in args.start.split(',')])
    stop = tuple([int(i) for i in args.stop.split(',')])

    print(main())


