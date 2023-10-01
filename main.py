from Graduation_Subclass import *
from superclass import *
from download_data import prereq_dict,units_dict,type_dict, course_names_list, depth_dict
from courses_to_units import courses_to_units
import heapq

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
# self.__dict__.update(total_courses = total_courses, state_courses=state_courses, g_value = g_value, h_value = h_value, parent=parent,path_cost=path_cost)
currentNode = Node(initial_state_courses_new_student, initial_state_courses_new_student, 0, 0, None)
semester_number = 0

def priorityQueue(expanded_nodes):
    priority_queue = []
    for node in expanded_nodes:
        heapq.heappush(priority_queue, (node.g_value + node.h_value, node))
    return priority_queue
    
problem.distance_from_graduation(currentNode.total_courses)
while(problem.is_goal(currentNode.total_courses) == False):
    semester_number += 1
    print("semester number:",semester_number)
    print("current node state:", currentNode.state_courses)
    print("total courses:",currentNode.total_courses)


    #print(problem.prerequisites)
    actions = problem.actions(currentNode.total_courses)
    print("actions:",actions)
    expanded_nodes = expand(problem, currentNode)
    '''
    for node in expanded_nodes:
        print("possible semester:",node.state_courses)
        print("f-value:",node.g_value + node.h_value)
        print("path-cost:",node.g_value)
        print("parent:",node.parent)
        print(" ")
    '''

    if semester_number == 1:
        TOTAL_PRIORITY_QUEUE = priorityQueue(expanded_nodes)
    else:
        combined_pq = list(heapq.merge(TOTAL_PRIORITY_QUEUE,priorityQueue(expanded_nodes) ))
        TOTAL_PRIORITY_QUEUE = combined_pq

    next_semester = heapq.heappop(TOTAL_PRIORITY_QUEUE)
    print("next semester:",next_semester)
    print("f-value:",next_semester[1].g_value + next_semester[1].h_value)
    currentNode = next_semester[1]
    #currentNode.total_courses = next_semester[1] + currentNode.total_courses  
    #print("LOOK HERE",next_semester)

