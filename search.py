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

import util
import random
import math

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
#    """Search the node of least total cost first."""

#    """take the first node
    firstNode = problem.getStartState()

#   	"""create the vectors"""
    visited = []
 #    """create a priority queue"""
    queue = util.PriorityQueue()

# 	"""include the first node with null heuristic in the priority queue"""
    queue.push((firstNode, []), nullHeuristic)
    
 #    """While the priority queue still have elements, keep doing the code below"""
    while not queue.isEmpty():

 #    	"""take from the queue the node and the action """
        node, steps = queue.pop()

        if node not in visited:
 #     	"""if the respective node is not in visited, then it is add"""
            visited.append(node)
 #     		"""verify if the node is the goal state, if so end the code"""
            if problem.isGoalState(node):
                print "solucao ", steps, "numero de estados ", len(steps) 
                return steps

            successors = problem.getSuccessors(node)
               
 #    		"""search for nodes the haven't been visited yet, so calculate the total cost  """
            for neighbor in successors:
                if not neighbor[0] in visited:
#			"""update the total cost"""
                    newSteps = steps + [neighbor[1]]
#    				"""add the node to the queue"""
                    queue.push((neighbor[0], newSteps), problem.getCostOfActions(newSteps))

    print "solucao ", steps, "numero de estados ", len(steps) 
    return steps

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    close_list=[]
    open_list=[]
    steps=[]

    queue=util.PriorityQueue()

    firstNode = problem.getStartState()

    queue.push((firstNode, []), heuristic(firstNode, problem))

    while not queue.isEmpty():

        node, steps = queue.pop()
       
        close_list.append(node)

        if problem.isGoalState(node):
            print "solucao ",  steps, "numero de estados ", len(steps)
            return steps

        open_list=problem.getSuccessors(node)

        for neighbors in open_list:
            if neighbors not in close_list:
                neighborSteps = steps + [neighbors[1]]
                cost = problem.getCostOfActions(neighborSteps) + heuristic(neighbors[0], problem)
                queue.push((neighbors[0], neighborSteps), cost)

    print "solucao ", steps
    return steps

def simulatedAnnelingSearch(problem, heuristic=nullHeuristic):
    alpha = 1.2
    t = 1.0
    queue=util.Queue()
    steps=[]
    state = problem.getStartState()
    
    action = []

    while True:
        queue=util.Queue()
        i=0
        neighbors = problem.getSuccessors(state)
        

        for nextStates in neighbors:
            auxDirection=[nextStates[1]]
            queue.push((nextStates[0], auxDirection))
            i = i+ 1

        randomPoint= random.randint(0, i-1)

        if randomPoint > 0:
            for successor in range (0, randomPoint + 1):
                newState, newaction = queue.pop()
        else:
            newState, newaction = queue.pop()

        e= problem.getCostOfActions(action) - problem.getCostOfActions(newaction)

        if e < 0:
            state= newState
            action= newaction
            steps = steps + action
        else:
            if math.exp(-e/t):
                state= newState
                action= newaction
                steps = steps + action

        if problem.isGoalState(state):
            print "solucao ", steps, "numero de estados " , len(steps)
            return steps

        t=t * alpha

    print "solucao ", steps, "numero de estados ", len(steps)
    return steps


def HillClimbingSearch(problem, heuristic=nullHeuristic):

    state=problem.getStartState()

    nextCost= 0
    cost = 1
    queue = util.PriorityQueue()
    steps=[]

    state= ((state, []), heuristic(state, problem))

    while cost > nextCost:
        queue = util.PriorityQueue()
        
        if problem.isGoalState(state):
           print "solucao ", steps, "numero de estados ", len(steps)           
           return steps

        cost = heuristic(state, problem)

        successors= problem.getSuccessors(state[0][0])

        for neighbor in successors:
            action_cost = problem.getCostOfActions([neighbor[1]]) + heuristic(neighbor[0], problem)
            queue.push((neighbor[0], neighbor[1]), action_cost)

        nextState = queue.pop()

        nextCost = problem.getCostOfActions([nextState[1]]) + heuristic(nextState[0], problem) - 1
    
    steps = steps + [nextState[1]]
    state = ((nextState[0], nextState[1]), nextCost)
    print "solucao ", steps, "numero de estados ", len(steps) 
    return steps


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
sa= simulatedAnnelingSearch
hc= HillClimbingSearch
