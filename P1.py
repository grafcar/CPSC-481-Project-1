import heapq
import pandas as pd

class Courses:
    def __init__(self, type, name, description, units, difficulty, prereqs):
        self.type = type
        self.name = name
        self.description = description
        self.units = units
        self.difficulty = difficulty
        self.prereqs = prereqs

    def get_type(self):
        return self.type
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_units(self):
        return self.units
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_prereqs(self):
        return self.prereqs

    def __str__(self):
        return f"Type: {self.type}\nName: {self.name}\nDescription: {self.description}\nUnits: {self.units}\nDifficulty: {self.difficulty}\nPrereqs: {self.prereqs}\n"
        
df = pd.read_excel('CPSC-481-Project-1/data.xlsx')
df = df.fillna('None')

courses = []

for _, row in df.iterrows():
    type = row['Type']
    name = row['Name']
    description = row['Description']
    units = row['Units']
    difficulty = row['Difficulty']
    prereqs = row['Prereq']

    courses.append(Courses(type, name, description, units, difficulty, prereqs))

for course in courses:
    print(course)

print(courses[1].get_name())