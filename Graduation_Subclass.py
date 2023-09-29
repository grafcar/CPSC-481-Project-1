from superclass import *
from itertools import combinations
from courses_to_units import courses_to_units


class GraduationPathProblem(Problem): # Inherit from the Problem class
    def __init__(self, initial, goal, prerequisites, course_units, course_type,course_depth):
        super().__init__(initial=initial, goal=goal)  # Call the parent class constructor
        self.course_units = course_units
        self.prerequisites = prerequisites
        self.course_type = course_type
        self.course_depth = course_depth

    #we need to keep track of the classes we have taken so far
    #we need to keep track of the classes we can take

    def actions(self, state):
        # Generate possible actions (courses to take) as long as they are not already taken and prerequisites are satisfied.
        actions = []

        for course in self.course_units:
            if course not in state:
                prerequisites = self.prerequisites.get(course)
                if prerequisites is None or (prerequisites == ['None'] and course not in state) or all(prereq in state for prereq in prerequisites):
                    actions.append(course)

        return actions


    def result(self, state, action):
        # Return the resulting state from taking an action (taking a course).
        return state + [action]

    def is_goal(self, state):
        # The goal is reached when the total units from all courses taken is 120.
        return sum(self.course_units[course] for course in state) == 120

    def action_cost(self, a):
        # The cost of an action is the number of units of the course.
        cost = -self.course_units[a]
        return cost

    def depth_heuristic(self, a):
        cost = -self.course_depth[a]
        return cost

    def balance_heuristic(self, node, actions, temp_list):
        possible_schedule = node.state_courses + temp_list
        courses_to_units(possible_schedule)
        #heuristic takes two values into account:
        #the depth of CS core courses
        #the balance of the course load - using given unit distribution dictionary

        #A STAR ALGORITHM:
        #tentative: It will generate a new priority heap for every chosen class
        #The chosen classes will be put into a temporary dictionary seperate from the node state
        #The chosen class will update the unit distribution
        pass

class courseNode:
    def __init__(self, state_courses,state_units,f_cost=None):
        self.__dict__.update(state_courses=state_courses,state_units=state_units, f_cost=f_cost)
