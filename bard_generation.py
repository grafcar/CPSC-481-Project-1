from textbook_python import *

class GraduationPathProblem(Problem): # Inherit from the Problem class
    def __init__(self, initial, goal, courses, prerequisites):
        super().__init__(initial=initial, goal=goal)  # Call the parent class constructor
        self.courses = courses
        self.prerequisites = prerequisites

    def actions(self, state):
        # Generate possible actions (courses to take) as long as they are not already taken and prerequisites are satisfied.
        actions = []
        for course in self.courses:
            if course not in state and all(prereq in state for prereq in self.prerequisites.get(course, [])):
                actions.append(course)
        return actions

    def result(self, state, action):
        # Return the resulting state from taking an action (taking a course).
        return state + [action]

    def is_goal(self, state):
        # The goal is reached when the total units from all courses taken is 120.
        return sum(self.courses[course] for course in state) == 120

    def action_cost(self, s, a, s1):
        # The cost of an action is the number of units of the course.
        # If the course has prerequisites, add an additional cost.
        cost = self.courses[a]
        if a in self.prerequisites:
            cost += len(self.prerequisites[a])
        return cost

    def h(self, node):
        # Heuristic: estimate the remaining units to reach 120.
        return 120 - sum(self.courses[course] for course in node.state)
    