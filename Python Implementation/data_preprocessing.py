import pandas as pd

# Read the Excel file
data = pd.read_excel('Data/data.xlsx', engine='openpyxl')

# Convert data into a list of dictionaries
courses_list = data.to_dict(orient='records')

# Print first course for verification
print(courses_list[0])

# Organizing the data based on the 'Type' of course
organized_courses = {}

for course in courses_list:
    course_type = course['Type']
    
    if course_type not in organized_courses:
        organized_courses[course_type] = []

    organized_courses[course_type].append(course)

# Printing the number of courses in each type for verification
for course_type, courses in organized_courses.items():
    print(f"{course_type}: {len(courses)} courses")