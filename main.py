import heapq
import random
from Graduation_Subclass import *
from superclass import *
from download_data import prereq_dict,units_dict,type_dict, course_names_list
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
problem = GraduationPathProblem(initial_state_courses_new_student, final_state_courses, prereq_dict, units_dict, type_dict)
# Initialize the priority queue to hold nodes, with the random values as priority 
priority_queue = []
# Initialize dictionary to store random values (for now)
r_values = {}

# Define the initial node can calculate r_value to add to priority queue
initial_node = Node(initial_state_courses_new_student)
r_values[tuple(initial_node.state_courses)] = random.randint(1, 100)  # Assign a random value
heapq.heappush(priority_queue, (r_values[tuple(initial_node.state_courses)], initial_node))
    
print("Initial Node:", initial_node.state_courses)
print("Initial Priority Queue:", priority_queue)
    
while priority_queue:
    # get node from lowest r_value from queue
    current_priority, currentNode = heapq.heappop(priority_queue)


    print("Current Node:", currentNode.state_courses)
        
    # Check to see if current node is the goal state, break if so
    if problem.is_goal(currentNode.state_courses):
        print("Goal reached!")

        break
        
    # Find possible actions and for current state
    actions = problem.actions(currentNode.state_courses)
    print("Available Actions:", actions)
    #explore new states
    for action in actions:
        #find resulting state from action
        resulting_state = problem.result(currentNode.state_courses, action)
            
        # If the resulting state is new, assign it a random f_value
        if tuple(resulting_state) not in r_values:
            r_values[tuple(resulting_state)] = random.randint(1, 100)
            
        # Create a new node and add it into the priority queue 
        new_node = Node(resulting_state, action, currentNode)
        heapq.heappush(priority_queue, (r_values[tuple(resulting_state)], new_node))

        #print the new node and update priority queue    
        print("New Node:", new_node.state_courses)
        print("Updated Priority Queue:", priority_queue)
    
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



#find the path from the initial state to the goal state - path_states(node)