import heapq
import pandas as pd
import itertools
from course_heuristics import estimate_remaining_semesters

class Node:
    def __init__(self, courses_taken, courses_left, g_value, max_units_per_semester, course_db ):
        self.courses_taken = courses_taken
        self.courses_left = courses_left
        self.g_value = g_value
        self.h_value = estimate_remaining_semesters(courses_left, max_units_per_semester, course_db)
        self.f_value = self.g_value + self.h_value

    def __lt__(self, other):
        return self.f_value < other.f_value

    def can_take(self, course, taken_courses):
        # Checking prerequisites
       if pd.isna(course["Prereq"]):
        return True
       else:
            prereqs = course["Prereq"].split(", ")
            return all(prerequisite in taken_courses for prerequisite in prereqs)

    def expand(self, course_db, max_units_per_semester):
        # Logic to expand the current node to generate possible future semesters
        next_possible_courses = []
        for course in self.courses_left:
            if self.can_take(course, self.courses_taken):
                next_possible_courses.append(course)

        possible_combinations = []  # This would store all possible sets of courses for next semester

        # Generate all possible combinations of courses ensuring they don't exceed max_units_per_semester
        # This is a simplistic approach and can be optimized.
        # Here, we are taking one course, two courses, and so on until max units are filled
        for i in range(1, len(next_possible_courses) + 1):
            for combo in itertools.combinations(next_possible_courses, i):
                if sum(course["Units"] for course in combo) <= max_units_per_semester:
                    possible_combinations.append(combo)

        nodes = []
        for combo in possible_combinations:
            nodes.append(Node(self.courses_taken + list(combo), 
                              [course for course in self.courses_left if course not in combo], 
                              self.g_value + 1))
        return nodes

def a_star_search(course_db, max_units_per_semester):
    initial_node = Node([], course_db, 0)
    frontier = [(initial_node.f_value, initial_node)]
    
    while frontier:
        _, current_node = heapq.heappop(frontier)
        
        if not current_node.courses_left:
            return current_node.courses_taken

        for next_node in current_node.expand(course_db, max_units_per_semester):
            heapq.heappush(frontier, (next_node.f_value, next_node))

    return None