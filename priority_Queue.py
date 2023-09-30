import heapq
#I based this code from the priority queue code of the textbook github respitory 
#https://github.com/aimacode/aima-python/blob/master/search4e.ipynb
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
