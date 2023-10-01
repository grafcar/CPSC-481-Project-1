from search import *
import pandas as pd
import copy

GOAL = 30
MAX_UNITS = 17
SEMESTER_CAP = 5

df = pd.read_excel('aima-python/smaller_data.xlsx')
df = df.fillna('None')

courses = []

for _, row in df.iterrows():
    name = row['Name']
    units = row['Units']
    prereqs = row['Prereq']
    courses_tuple = (name, units, prereqs)
    courses.append(courses_tuple)

print(courses)

# Define the state representation as a list of completed courses
# Define the state representation as a list of completed courses and total units
class GraduationState:
    def __init__(self, completed_courses=None, total_units=0, selected_courses=None):
        self.completed_courses = completed_courses or []
        self.total_units = total_units  # Initialize the total units attribute
        self.selected_courses = selected_courses or []  # Initialize the selected courses attribute


    def __lt__(self, other):
        return self.total_units < other.total_units

# Define the goal state as reaching the desired total units (e.g., 120 units)
goal_units = 120
goal_state = GraduationState(total_units=goal_units)


# Define the initial state (e.g., for a first-time freshman with no completed courses)
initial_state = GraduationState()

courses = [('Class 1', 3, 'None'), ('Class 2', 3, 'None'), ('Class 3', 3, 'None'), 
           ('Class 4', 3, 'None'), ('Class 5', 3, 'None'), ('Class 6', 3, 'None'),
           ('Class 7', 3, 'None'), ('Class 8', 3, 'None'), ('Class 9', 3, 'None'),
           ('Class 10', 3, 'None')]

# Define the list of required courses for graduation
# Each course is represented as a tuple (course_name, prerequisites, units)
# For simplicity, we assume each course is worth 3 units

# Define a function to generate possible actions (taking available courses)
def generate_actions(state):
    global courses
    # Get the first 5 classes that have 'None' as a prerequisite and have not been previously selected
    available_classes = [c for c in courses if c[2] == 'None' and c[0] not in state.completed_courses][:5]
    
    # Add these classes to the list of selected courses
    state.completed_courses.extend([c[0] for c in available_classes])
    
    # Now, update the prerequisites of the remaining classes
    for i in range(len(courses)):
        if courses[i][2] in [c[0] for c in available_classes]:
            # If a class had one of the taken classes as a prerequisite, set its prerequisite to 'None'
            courses[i] = (courses[i][0], courses[i][1], 'None')
    
    return available_classes


def apply_action(state, action):
    new_state = GraduationState(completed_courses=state.completed_courses + [action],
                                total_units=state.total_units + action[1],
                                selected_courses=state.selected_courses)
    print("Applied action:", state.total_units)
    return new_state



# Define a heuristic function to estimate the remaining semesters needed to graduate
# def heuristic(state):
#     remaining_units = 0
#     for course in courses:
#         course_name, units, _ = course
#         if course_name not in state.completed_courses:
#             print("remaining units:", remaining_units, "units:", units)
#             remaining_units += units
def heuristic(state):
    print("h state", state.total_units)
    remaining_units = GOAL - state.total_units
    print("remaining units:", remaining_units)
    # Assuming a student can take a maximum of 17 units per semester
    remaining_semesters = remaining_units // MAX_UNITS
    print("remaining semesters:", remaining_semesters)
    return remaining_semesters


# Import the A* search function from your provided code


# Create the problem instance
class GraduationProblem(Problem):
    def __init__(self, initial, goal, actions, heuristic):
        super().__init__(initial, goal)
        self.actions = actions
        self.heuristic = heuristic

    def result(self, state, action):
        return apply_action(state, action)

    def goal_test(self, state):
        return state.total_units >= self.goal.total_units

    def actions(self, state):
        return generate_actions(state)

    def h(self, node):
        return self.heuristic(node.state)

# Define the goal state (empty list, indicating all required courses are completed)
# Define the goal state as reaching the desired total units
# goal_state = GraduationState(completed_courses=[], total_units=GOAL)


# Create the problem instance
problem = GraduationProblem(initial_state, goal_state, generate_actions, heuristic)

# Solve the problem using A* search
solution_node = astar_search(problem)

# Extract the optimal path to graduation from the solution_node

if solution_node:
    optimal_path = solution_node.path()
    # Extract and print the actions taken in each step
    for step, node in enumerate(optimal_path):
        if node.action:
            print(f"Semester {step + 1}: {node.action}")
    print("Optimal path found!")
else:
    print("No solution found.")
