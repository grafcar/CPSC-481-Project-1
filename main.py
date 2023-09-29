from Graduation_Subclass import *
from superclass import *
from download_data import prereq_dict,units_dict,type_dict, course_names_list, depth_dict
from courses_to_units import courses_to_units

# Define the initial state (courses already taken)
#We will use 3 different initial states to test our algorithm

#INITIAL STATES
initial_state_courses_new_student = [] # we only need courses in the state, because we can always find the units for each course and the prerequisites for each course from the courses dictionary and the prerequisites dictionary

#int 1 = Core CS courses        - 66 units
#int 2 = CS elective courses    - 15 units
#int 3 = science/math elective  - 12 units
#int 4 = general education      - 24 units
#int 5 = graduation requirement - 3 units 
#                         total - 120 units

initial_state_unit_dict = {
        "CS Core Course": 0,
        "CS Electives": 0,
        "Science/Math Elective": 0,
        "General Education": 0,
        "Graduation Requirement": 0
    }

#GOAL STATES
final_state_units_dict = {
    "CS Core Course": 66,
    "CS Electives": 15,
    "Science/Math Elective": 12,
    "General Education": 24,
    "Graduation Requirement": 3
}

final_state_courses = course_names_list


#initial_state_transfer_student
#initial_state_Mike_Ball 

# Instantiate the GraduationPathProblem
problem = GraduationPathProblem(initial_state_courses_new_student, final_state_courses, prereq_dict, units_dict, type_dict,depth_dict)

############################################################################################

#0 define the root node
#1 check if the state of the new node is the goal state
#2 use a priority queue to find the best actions to take from the current node
    # 2.1 find the list of all possible classes, considering prerequisites and previous courses taken already
    # 2.2 find f-cost of each course using cost function and heuristic function
    # 2.3 organize each course into a priority queue
    # 2.4 pick the course that is highest in the priority queue
    # 2.5 create priority queue again with new course
    # 2.6 continue doing this until unit limit is reached
#3 Create new Node and assign the new schedule to it's state
#4 Assign new Node as the child of the previous node
#5 Go back to step 1

############################################################################################

# 0. define the initial state - node.state
currentNode = Node(initial_state_courses_new_student)
print("test")
print("state:", currentNode.state_courses)


#print(problem.prerequisites)
actions = problem.actions(currentNode.state_courses)
print("actions:",actions)


single_course_nodes = expand(problem,currentNode) #generates a list of nodes which represent possible classes to add
#print("Nodes:",expand(problem,currentNode))
for node in single_course_nodes:
    print("Node Course:",node.state_courses)
    print("Node Path Cost:",node.path_cost)
#find the path from the initial state to the goal state - path_states(node)