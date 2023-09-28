from bard_generation import *
from textbook_python import *

# Define the initial state (courses already taken)
#We will use 3 different initial states to test our algorithm
initial_state_new_student = [] # we only need courses in the state, because we can always find the units for each course and the prerequisites for each course from the courses dictionary and the prerequisites dictionary
#initial_state_transfer_student
#initial_state_Mike_Ball 

# Define the goal state (graduation requirement)
goal_state = 120  # Total units required for graduation

# Define the courses and their associated units
courses = {
    "CPSC120": 4,
    "MATH150": 3,
    # Add more courses and units as needed
}

# Define course prerequisites
prerequisites = {
    "CPSC121": ["CPSC120"],
    "CPSC131": ["CPSC120"],
    # Add more prerequisites as needed
}

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
print("test")
while problem.is_goal(currentNode.state) != True:
    problem.actions(currentNode.state)


#find the path from the initial state to the goal state - path_states(node)