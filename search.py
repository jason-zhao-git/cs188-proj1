# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from typing import Tuple
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()
class Node:
    def __init__(self, posi, parent = None, dir = None, cost = 0):
        self.posi = posi
        self.parent = parent
        self.direction = dir
        self.cost = cost


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    '''util.raiseNotDefined()'''
    from util import Stack
   
    result = []
    curr_pos = problem.getStartState()
    curr_pos = Node(curr_pos)
    stack = Stack()
    explored = set()
    
    stack.push(curr_pos)
    while (not stack.isEmpty()):
        curr = stack.pop()
        if (problem.isGoalState(curr.posi)):
            break
        if curr.posi in explored:
            continue
       
        explored.add(curr.posi)
        for valid_nxt in problem.getSuccessors(curr.posi):
            stack.push(Node(valid_nxt[0], curr, valid_nxt[1], valid_nxt[2]))
    
    if (problem.isGoalState(curr.posi)):
        while curr.parent != None:
            result.insert(0, curr.direction)
            curr = curr.parent
    
    return result



def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
   
    result = []
    curr_pos = problem.getStartState()
    curr_pos = Node(curr_pos)
    queue = Queue()
    explored = set()
    
    queue.push(curr_pos)
    while (not queue.isEmpty()):
        curr = queue.pop()
        if (problem.isGoalState(curr.posi)):
            break
        if curr.posi in explored:
            continue
       
        explored.add(curr.posi)
        for valid_nxt in problem.getSuccessors(curr.posi):
            queue.push(Node(valid_nxt[0], curr, valid_nxt[1], valid_nxt[2]))
    
    if (problem.isGoalState(curr.posi)):
        while curr.parent != None:
            result.insert(0, curr.direction)
            curr = curr.parent
    
    return result

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
   
    result = []
    curr_pos = problem.getStartState()
    curr_pos = Node(curr_pos)
    queue = PriorityQueue()
    explored = set()
    
    queue.push(curr_pos, curr_pos.cost)
    while (not queue.isEmpty()):
        curr = queue.pop()
        if (problem.isGoalState(curr.posi)):
            break
        if curr.posi in explored:
            continue
       
        explored.add(curr.posi)
        for valid_nxt in problem.getSuccessors(curr.posi):
            priority = curr.cost + valid_nxt[2]
            queue.push(Node(valid_nxt[0], curr, valid_nxt[1], priority), priority)
    
    if (problem.isGoalState(curr.posi)):
        while curr.parent != None:
            result.insert(0, curr.direction)
            curr = curr.parent
    
    return result

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
   
    result = []
    curr_pos = problem.getStartState()
    curr_pos = Node(curr_pos, None, None, heuristic(curr_pos, problem))
    queue = PriorityQueue()
    explored = set()
    
    queue.push(curr_pos, heuristic(curr_pos.posi, problem))
    while (not queue.isEmpty()):
        curr = queue.pop()
        if (problem.isGoalState(curr.posi)):
            break
        if curr.posi in explored:
            continue
       
        explored.add(curr.posi)
        for valid_nxt in problem.getSuccessors(curr.posi):
            priority = curr.cost + valid_nxt[2]
            queue.push(Node(valid_nxt[0], curr, valid_nxt[1], priority), priority + heuristic(valid_nxt[0], problem))
    
    if (problem.isGoalState(curr.posi)):
        while curr.parent != None:
            result.insert(0, curr.direction)
            curr = curr.parent
    
    return result


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
