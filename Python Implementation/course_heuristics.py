import math

def estimate_remaining_semesters(remaining_courses, max_units_per_semester, all_courses):
    # Basic estimation by units
    total_remaining_units = sum(course["Units"] for course in remaining_courses)
    semesters_by_units = math.ceil(total_remaining_units / max_units_per_semester)
    
    # Penalty for course difficulty
    difficulty_penalty = sum(course["Difficulty"] for course in remaining_courses) / len(remaining_courses)

    # Penalty for prerequisites
    prerequisite_penalty = 0
    for course in remaining_courses:
        is_prerequisite_for = sum(1 for other_course in all_courses if other_course["Prereq"] == course["Name"])
        prerequisite_penalty += is_prerequisite_for

    # Combining the penalties (this is a basic approach and the weights can be adjusted based on preferences)
    total_penalty = 0.1 * difficulty_penalty + 0.9 * prerequisite_penalty  # Here, I'm giving more weight to prerequisites
    
    # Return the heuristic value
    return semesters_by_units + total_penalty