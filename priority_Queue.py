import heapq
#I based this code from the textbook github respitory 
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