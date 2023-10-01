from search import *
import pandas as pd

GOAL = 120
MAX_UNITS = 17
SEMESTER_CAP = 5

df = pd.read_excel('aima-python/data.xlsx')
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
    def __init__(self, completed_courses=None, total_units=0,semester_classes=None):
        self.completed_courses = completed_courses or []
        self.total_units = total_units  # Initialize the total units attribute
        self.semester_classes = semester_classes or [[]]

# Define the goal state as reaching the desired total units (e.g., 120 units)
goal_units = 120
goal_state = GraduationState(total_units=goal_units)


# Define the initial state (e.g., for a first-time freshman with no completed courses)
initial_state = GraduationState()

# Define the list of required courses for graduation
# Each course is represented as a tuple (course_name, prerequisites, units)
# For simplicity, we assume each course is worth 3 units

# Define a function to generate possible actions (taking available courses)
def generate_actions(state):
    taken_classes = []
    global courses
    # Initialize the total units
    total_units = 0
    
    # While the student has taken less than 120 units
    while total_units < 120:
        # Get the first 5 classes that have 'None' as a prerequisite
        available_classes = [c for c in courses if c[2] == 'None'][:SEMESTER_CAP]
        
        # Add these classes to the list of classes the student has taken
        taken_classes.extend(available_classes)
        
        # Add their units to the total units
        total_units += sum(c[1] for c in available_classes)
        
        # Remove these classes from the list of all classes
        courses = [c for c in courses if c not in available_classes]
        
        # Now, update the prerequisites of the remaining classes
        for i in range(len(courses)):
            if courses[i][2] in [c[0] for c in available_classes]:
                # If a class had one of the taken classes as a prerequisite, set its prerequisite to 'None'
                courses[i] = (courses[i][0], courses[i][1], 'None')
    
    return taken_classes

# Define a function to apply an action (update the state)
def apply_action(state, action):
    state.completed_courses.extend(action)
    # state.semester_units += action[1]
    # print("Semester Units:", state.semester_units)
    # if state.semester_units >= MAX_UNITS:
    #     state.semester_units = 0
    #     return state
    state.total_units += action[1]
    print("Applied action:", action)
    print("State:", state)
    print("State completed courses:", state.completed_courses)
    print("Applied actions total units:", state.total_units)
    return state

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
    remaining_units = goal_units - state.total_units
    print("remaining units:", remaining_units)
    # Assuming a student can take a maximum of 17 units per semester
    remaining_semesters = (remaining_units + 16) // 17
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
