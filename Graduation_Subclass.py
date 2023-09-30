from superclass import *
from itertools import combinations
from courses_to_units import courses_to_units
from download_data import type_dict

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
    
    def possible_semesters(self, actions):
        # Generate all possible semesters given possible courses to take.
        # The semester cannot have more than 17 units and must have at least 12 units.
        # The semesters will be represented as a list of lists of courses.
        # The function returns a list of lists of courses.
        valid_semesters = []

        for r in range(1, min(8, len(actions) + 1)):
            for course_combination in combinations(actions, r):
                if sum(self.course_units[course] for course in course_combination) <= 17:
                    valid_semesters.append(list(course_combination))

        return valid_semesters



    def result(self, state, action):
        # Return the resulting state from taking an action (taking a course).
        return state + [action]

    def is_goal(self, state):
        # The goal is reached when the total units from all courses taken is 120.
        return sum(self.course_units[course] for course in state) == 120

    def action_cost(self, a):
        # The cost of an action is the number of units of the course.
        cost = 10
        return cost

    def depth_heuristic(self, semester):
        cost = 0
        for course in semester:
            cost += self.course_depth[course]
        return -cost
    
    def semester_size_heuristic(self,semester):
        cost = 0
        for course in semester:
            cost += self.course_units[course]
        cost = 17 - cost
        return cost
    
    def balance_heuristic_short_term(self, semester):
        #This will only check for balance within the semester
        print("semester:",semester)
        unit_dict = courses_to_units(semester)
        if(unit_dict["CS Core Courses"] < 12):
            return -3
        else:
            return 3
    def balance_heuristic_long_term(self, semester, total_courses):
        #This will check for balance considering the total courses taken
        pass
'''
    def balance_heuristic_legacy(self, action, possible_schedule):
        #possible_schedule = node.state_courses + temp_list
        #print("possible schedule:",possible_schedule)
        unit_dictionary = courses_to_units(possible_schedule)
        print("Unit Dictionary:",unit_dictionary)
        #print("dictionary member:",type_dict[action])
        if(type_dict[action] in ["Upper Division Core", "Lower Division Core", "Math Requirements"] ):
            print("Core CS Class")
            Core_Units_Left = 66 - unit_dictionary["CS Core Courses"]
            print(unit_dictionary["CS Core Courses"])
            print(Core_Units_Left)
            return -Core_Units_Left / 4
        elif(type_dict[action] == "CS Electives"):
            print("CS Elective")
            CS_Elective_Units_Left = 15 - unit_dictionary["CS Electives"]
            print(CS_Elective_Units_Left)
            return -CS_Elective_Units_Left / 4
        elif(type_dict[action] == "Science/Math Elective"):
            print("Science/Math Class")
            ScienceMath_Units_Left = 12 - unit_dictionary["Science/Math Elective"]
            print(ScienceMath_Units_Left)
            return -ScienceMath_Units_Left / 4
        elif(type_dict[action] == "General Education"):
            print("Gen Ed")
            GE_Units_Left = 24 - unit_dictionary["General Education"]
            print(GE_Units_Left)
            return -GE_Units_Left / 4
        elif(type_dict[action] == "Graduation Requirement"):
            print("Grad Requirement")
            Graduation_Requirement_Units_Left = 3 - unit_dictionary["Graduation Requirement"]
            print(Graduation_Requirement_Units_Left)
            return -Graduation_Requirement_Units_Left / 4
        else:
            print("Error Occured")
            #print("Dictionary Type:",type_dict[action])
            return False
        #heuristic takes two values into account:
        #the depth of CS core courses
        #the balance of the course load - using given unit distribution dictionary

        #A STAR ALGORITHM:
        #tentative: It will generate a new priority heap for every chosen class
        #The chosen classes will be put into a temporary dictionary seperate from the node state
        #The chosen class will update the unit distribution
'''


class courseNode:
    def __init__(self, state_courses,state_units,f_cost=None):
        self.__dict__.update(state_courses=state_courses,state_units=state_units, f_cost=f_cost)
