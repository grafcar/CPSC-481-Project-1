from superclass import *
from itertools import combinations



class GraduationPathProblem(Problem): # Inherit from the Problem class
    def __init__(self, initial, goal, prerequisites, course_units, course_type):
        super().__init__(initial=initial, goal=goal)  # Call the parent class constructor
        self.course_units = course_units
        self.prerequisites = prerequisites
        self.course_type = course_type

    #we need to keep track of the classes we have taken so far
    #we need to keep track of the classes we can take

    def actions(self, state):
        # Generate possible actions (courses to take) as long as they are not already taken and prerequisites are satisfied.
        actions = []
        possible_actions = []

        #things to keep in mind:
        #courses already taken
        #courses not yet satisfied by prerequisites
        for course in self.course_units:
            if course not in state and all(courses in state for courses in self.prerequisites.get(course, [])):
                possible_actions.append(course)

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

    def h(self, node, actions):
        pass

class courseNode:
    def __init__(self, state_courses,state_units,f_cost=None):
        self.__dict__.update(state_courses=state_courses,state_units=state_units, f_cost=f_cost)
