from superclass import *
from itertools import combinations



class GraduationPathProblem(Problem): # Inherit from the Problem class
    def __init__(self, initial, goal, course_units, prerequisites):
        super().__init__(initial=initial, goal=goal)  # Call the parent class constructor
        self.course_units = course_units
        self.prerequisites = prerequisites

    #we need to keep track of the classes we have taken so far
    #we need to keep track of the classes we can take
    def generate_all_combinations(self, state):
        actions = []
        
        # Generate a list of available courses that are not already taken and have satisfied prerequisites
        available_courses = [course for course in self.course_units if course not in state and all(prereq in state for prereq in self.prerequisites.get(course, []))]
        
        # Generate all possible combinations of courses
        for r in range(1, min(9,len(available_courses) + 1)):
            for combo in combinations(available_courses, r):
                # Calculate the total units for this combination
                combo_units = sum(self.course_units[course] for course in combo)
                
                # Check if the total units do not exceed the maximum allowed units
                if combo_units <= 17:
                    actions.append(list(combo))  # Append the combination as a list
        return actions


    def actions(self, state):
        # Generate possible actions (courses to take) as long as they are not already taken and prerequisites are satisfied.
        actions = []
        possible_actions = []
        num_units = 0
        #needs to be reworked. actions should be a list of lists, where each list is a possible combination of courses to take

        for course in self.course_units:
            if course not in state and all(prereq in state for prereq in self.prerequisites.get(course, [])):
                possible_actions.append(course)

        while num_units < 17:
            pass

        return actions

    def result(self, state, action):
        # Return the resulting state from taking an action (taking a course).
        return state + [action]

    def is_goal(self, state):
        # The goal is reached when the total units from all courses taken is 120.
        return sum(self.course_units[course] for course in state) == 120

    def action_cost(self, s, a, s1):
        # The cost of an action is the number of units of the course.
        # If the course has prerequisites, add an additional cost.
        cost = self.course_units[a]
        if a in self.prerequisites:
            cost += len(self.prerequisites[a])
        return cost

    def h(self, node):
        # Heuristic: estimate the remaining units to reach 120.
        returnVal = 120 - sum(self.course_units[course] for course in node.state)
        return returnVal
    