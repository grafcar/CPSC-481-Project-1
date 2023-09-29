import heapq

#Used the code from the github respitory of the textbook

class priorityQueue:
     def __init__(self, actions):
          self.actions = []
          for action in actions:
               self.add(action)
          heapq.heapify(actions)

     def pop(self):
         return heapq.heappop(self.actions)
    
     def add(self, action):
         return heapq.heappush(self.actions, action)

#courses = { "CPSC120": 4, "MATH150": 3, "CPSC121": 3, "CPSC131": 3, "CPSC120": 2}
#print(sorted(courses, reverse = True))
#course_list = list(courses.items())
#heapq.heapify(course_list)
#print(sorted(course_list, reverse = True))
#print(heapq.heappop(sorted(course_list, reverse = True)))
#print(sorted(course_list, reverse = True))
#print(course_list)
#course_dict = dict(course_list)
#print(sorted(course_dict, reverse = True))

#courses = {"MATH150": 3, "CPSC121": 3, "CPSC131": 2, "CPSC120": 4}
course_list = [1, 3, 4, 2, 5, 2, 3, 3, 3, 3, 3, 3]
#course_list = list(courses.items())
#heapq.heapify(course_list)
queue = priorityQueue(course_list)
#for a in course_list:
#    queue.add(a)
#queue.pop()
#queue.pop()
print(queue.actions)