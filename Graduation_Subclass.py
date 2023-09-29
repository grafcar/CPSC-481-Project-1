from superclass import *
from data import *

class GraduationPathProblem(Problem): # Inherit from the Problem class
    def __init__(self, initial, goal, courses, prerequisites):
        super().__init__(initial=initial, goal=goal)  # Call the parent class constructor
        self.courses = courses
        self.prerequisites = prerequisites
        self.types = types

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

    def action_cost(self, current_node, course, resulting_state):
        # The cost of an action is the number of units of the course.
        # If the course has prerequisites, add an additional cost.   // I'M NOT DOING THIS
        cost = self.courses[course]
        #if course in self.prerequisites:
        #    cost += len(self.prerequisites[course])
        return cost

    #def h(self, node):
    def h(self, node):
        # Heuristic: estimate the remaining units to reach 120.
        #return 120 - sum(self.courses[course] for course in node.state)

        # The node state represents the state of the problem at this node, so the list of classes a student plans to take
        #print("Node state: " + str(node.state))
        #heuristic_value = 0    
        # Calculate the heuristic value for each course in the remaining courses.
        for course in self.courses:
            if course not in node.state:
                heuristic_value = 0  
                # If the course has no prerequisites, assign a heuristic value of 4.
                if len(self.prerequisites[course]) == 0:
                    heuristic_value += 4
                else:
                    # If the course has prerequisites, assign a heuristic value of 4 - len(prerequisites).
                    result = 4 - len(self.prerequisites[course])
                    heuristic_value += result

                if self.types == "LowerDivisionCore" or self.types == "GeneralEducation" or self.types == "Science/MathElective":
                    heuristic_value += 3
                elif self.types == "CSElectives" or "GraduationRequirement":
                    heuristic_value += 2
                else:
                    heuristic_value += 1   #for upper core and math classes
        return heuristic_value
    
    def astar_search(problem):
        open_list = []  # Priority queue of frontier
        closed_list = set()

        # Initialize the open list with the initial state and its estimated cost.
        initial_node = Node(problem.initial)
        initial_node.cost_so_far = 0
        initial_node.heuristic_value = problem.h(initial_node)
        heapq.heappush(open_list, initial_node)

        while open_list:
            current_node = heapq.heappop(open_list)

            if problem.is_goal(current_node.state):
                return current_node.state

            closed_list.add(tuple(current_node.state))

            # Generate possible actions and resulting nodes.
            for action in problem.actions(current_node.state):
                resulting_state = problem.result(current_node.state, action)

                if tuple(resulting_state) not in closed_list:
                    # Create a new node for the resulting state.
                    next_node = Node(resulting_state)
                    #print("Resulting node: " + str(next_node))
                    next_node.cost_so_far = current_node.cost_so_far + problem.action_cost(current_node, action, next_node)
                    #print("Cost so far to resulting node: " + str(next_node.cost_so_far))
                    next_node.heuristic_value = problem.h(next_node)
                    #print("heuristic_value of resulting node: " + str(next_node.heuristic_value))

                    # Add the resulting node to the open list.
                    heapq.heappush(open_list, next_node)

        return None

    
    """
    def search(self):
        heapq.heappush(self.open_list, (0, self.initial_state))
        while self.open_list:
            _, current_state = heapq.heappop(self.open_list)
            
            if self.is_goal_state(current_state):
                # We've reached the goal state.
                return current_state
            
            if current_state in self.closed_list:
                continue
            
            self.closed_list.add(current_state)
            
            # Generate possible actions from the current state.
            for action in self.generate_actions(current_state):
                next_state = self.transition(current_state, action)
                if next_state not in self.closed_list:
                    g_cost = self.cost(current_state, action)
                    h_cost = self.heuristic(next_state)
                    f_cost = g_cost + h_cost
                    heapq.heappush(self.open_list, (f_cost, next_state))
        
        # If the open list is empty and no goal is found, return None.
        return None
        """
                
    