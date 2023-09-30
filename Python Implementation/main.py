from data_preprocessing import courses_list
from a_star_search import a_star_search

max_units_per_semester = 15  # assuming for this example
schedule = a_star_search(courses_list, max_units_per_semester)

if schedule:
    print("Optimal course schedule:", schedule)
else:
    print("No possible schedule found.")
    