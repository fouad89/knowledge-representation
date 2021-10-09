# ----------------------------------------------------------------
# function SIMPLE-PROBLEM-SOLVING-AGENT(percept ) returns an action
# persistent: seq, an action sequence, initially empty
#   state, some description of the current world state
#   goal , a goal, initially null
#   problem, a problem formulation
# state←UPDATE-STATE(state, percept )
# if seq is empty then
#   goal ←FORMULATE-GOAL(state)
#   problem ←FORMULATE-PROBLEM(state, goal )
#   seq ←SEARCH(problem)
# if seq = failure then return a null action
# action ←FIRST(seq)
# seq ←REST(seq)
# ----------------------------------------------------------------

import sys
from collections import deque

from utils import *

class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def action(self, state):
        """List of actions
        """

        return NotImplementedError

    def result(self, state, action):
        """Transition model description of what each action does
        """

        return NotImplementedError

    def goal_test(self, state):
        """determines whether a given state is a goal state
        """
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Assigns a numeric cost to each path
        """
        return c+1


# ----------------------------------------------------------------
class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

        # set depth at 0
        self.depth = 0
        # if the node is a parent, add 1 to depth
        if parent:
            self.depth = self.depth + 1


    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node

        Args:
            problem ([type]): [description]
        """
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_state = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """return the sequence of actions from root to this node
        """
        return [node.action for node in self.path()[:1]]

    def path(self):
        node = self
        path_back = []
        # going up the the path
        while node:
            path_back.append(node)
            node = node.parent
            return list(reversed(path_back))


    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)


# ______________________________________________________________________________
# Uninformed Search algorithms

def bds(problem):
    frontier = deque([Node(problem.initial)])

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None


def dfs(problem):
    frontier = deque([Node(problem.initial)])
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None
        
