# project2.py
# Ethan Sayles
# February 16, 2018
#
# Purpose: Create a program that utilizes various searching algorithms to find the optimal solution through a terrain.

import argparse
import numpy as np
import search as aima


class Search(aima.Problem):
    """Subclass of Problem that pertains to this project"""

    def __init__(self, initial, goal, filename):
        """The constructor inherits from the Problem class,
        passing the initial and goal states as tuples the the parent
        constructor. The filename is a string csv file"""

        aima.Problem.__init__(self, initial, goal)
        self.graph = np.loadtxt(filename, delimiter=',')
        self.width = len(self.graph[0])
        self.height = len(self.graph)

    def actions(self, state):
        """Return the possible directions given the current state. These directions
        are tuples that contain the amount in a direction that should change. e.g. 'up'
         is (0,-1) because the x value does not change, and the y value is decremented"""

        # The four corners:
        if state == (0, 0):
            #          d      dr      r
            return [(0, 1), (1, 1), (1, 0)]
        elif state == (0, self.height - 1):
            #          u      ur      r
            return [(0, -1), (1, -1), (1, 0)]
        elif state == (self.width - 1, 0):
            #          d       dl       l
            return [(0, 1), (-1, 1), (-1, 0)]
        elif state == (self.width - 1, self.height - 1):
            #          u        ul        l
            return [(0, -1), (-1, -1), (-1, 0)]

        # The left, right, top, and bottom edges:
        elif state[0] == 0:
            #          u       ur       r       dr      d
            return [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
        elif state[0] == self.width - 1:
            #          u         ul       l        dl      d
            return [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
        elif state[1] == 0:
            #          l        dl       d      dr       r
            return [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]
        elif state[1] == self.height - 1:
            #          l        ul        u       ur       r
            return [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)]

        # Any interior locations
        else:
            #          u        ul        l        dl      d       dr      r       ur
            return [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    def result(self, state, action):
        """Returns the output state given the current state and an action"""

        # New state is a tuple of the current state and the direction
        new_state = (state[0] + action[0], state[1] + action[1])

        # if the speed of the new state is 0, return the current state (don't go anywhere)
        if self.graph[new_state[1]][new_state[0]] != 0:
            return new_state
        else:
            return state

    def path_cost(self, c, state1, action, state2):
        """Return the total solution cost required to traverse from state1 to state2
        given an action, and a cost up to this point."""
        sp1 = self.graph[state1[1]][state1[0]]
        sp2 = self.graph[state2[1]][state2[0]]

        # Prevent division by zero error
        if sp2 == 0:
            return c + aima.infinity

        # Check if horizontal or vertical movement
        if action in ['d', 'r', 'u', 'l']:

            # Equation is derived from the distance horizontally/vertically times the sum of
            # the inverse of the speeds. This results in a time for travel.
            return c + 1/2 * (1/sp1 + 1/sp2)
        else:

            # Equation is derived from the distance diagonally times the sum of
            # the inverse of the speeds. This results in a time for travel.
            return c + 1/np.sqrt(2) * (1/sp1 + 1/sp2)

    def h(self, node):
        """Heuristic function that calculates straight-line distance from a node's state to the goal."""

        return aima.distance(node.state, self.goal)


def main():
    """Default function to be called when the program executes."""

    # Create an instance of the Search class with arguments from argparse
    searcher = Search(start, stop, args.grid)

    # Return the correct searching algorithm for a given specification
    if args.alg == 'bfs':
        search = aima.breadth_first_search(searcher)
    elif args.alg == 'ucs':
        search = aima.uniform_cost_search(searcher)
    else:
        search = aima.astar_search(searcher)
    return search.path()


if __name__ == '__main__':

    # Arguments for argparse.
    parser = argparse.ArgumentParser(description='Plan a route through a grid.')
    parser.add_argument("grid", help="map/grid filename (a CSV file")
    parser.add_argument("start", help="starting location as a pair r,c")
    parser.add_argument("stop", help="ending location as a pair r,c")
    parser.add_argument("--alg", default='a_star', help="algorithm to use to search (default: a_star)")

    args = parser.parse_args()

    # need to pass tuples to the search class
    start = tuple([int(i) for i in args.start.split(',')])
    stop = tuple([int(i) for i in args.stop.split(',')])

    # Will print the path traversed by the algorithm
    print(main())


