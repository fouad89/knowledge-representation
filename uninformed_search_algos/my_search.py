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