from Graduation_Subclass import *
from superclass import *
from data import *

# Define the initial state (courses already taken)
#We will use 3 different initial states to test our algorithm
#initial_state_new_student = [] # we only need courses in the state, because we can always find the units for each course and the prerequisites for each course from the courses dictionary and the prerequisites dictionary
initial_state_new_student = ["CPSC253"]
#initial_state_transfer_student
#initial_state_Mike_Ball 

# Define the goal state (graduation requirement)
goal_state = 120  # Total units required for graduation

# Instantiate the GraduationPathProblem
problem = GraduationPathProblem(initial_state_new_student, goal_state, courses, prerequisites)

############################################################################################

# 0. define the root node - node.state
# 1. check if a state is the goal state - problem.is_goal(node.state)
# 2. find actions to take from current node - problem.actions(node.state)
# 3. use the expand function to generate the children nodes - expand(problem, node)
# 4. find the resulting state from taking an action - problem.result(node.state, action)
# 5. find the cost of an action - problem.action_cost(node.state, action, resulting_state)
# 6. find the heuristic value of a node - problem.h(node)
# 7. combine the cost and heuristic value of each node
# 8. choose the node with the lowest cost + heuristic value
# 9. repeat steps 1-8 until the goal state is reached

############################################################################################

# 0. define the initial state - node.state
currentNode = Node(initial_state_new_student)

# 1. check if a state is the goal state - problem.is_goal(node.state)
print("Actions you can make:")
#This prints out all possible actions we can take from the current node
# When our initial state = no classes taken, we can only take classes that do not require prerequisites
print(problem.actions(currentNode.state))

#while problem.is_goal(currentNode.state) != True:
if problem.is_goal(currentNode.state) != True:
    actions = problem.actions(currentNode.state)
    
# We list out all actions we can take from the current node, choosing the one with the lowest f(n) cost to explore/expand
#iterate through the actions and find the resulting state, cost, and heuristic value for each action
for action in actions:
    resulting_state = problem.result(currentNode.state, action)
    cost = problem.action_cost(currentNode.state, action, resulting_state)
    #heuristic_value = problem.h(currentNode)
    heuristic_value = problem.h(currentNode)
    total_cost = cost + heuristic_value
    print("current node: " + str(currentNode.state))
    print("action: " + str(action))
    print("Action cost (units): " + str(cost))
    print("heuristic value: " + str(heuristic_value))
    print("total cost: " + str(total_cost))
    print("resulting state: " + str(resulting_state))
    print(" ")

result = problem.astar_search()
if result:
    print("Shortest path to graduation: ", result)
else:
    print("No path to graduation found.")