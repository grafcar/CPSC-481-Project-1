import heapq
from data import *

class AStarSearch:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        # open_list is the frontier of discovered nodes we haven't expanded
        self.open_list = []
        # closed_list contains states that have already been explored
        self.closed_list = set()
    
    def heuristic(self, state):
        # Define your heuristic function here.
        # It should estimate the cost from 'state' to the goal.

        pass

    def cost(self, state, action):
        # Define your cost function here.
        pass
    
    def is_goal_state(self, state):
        # Check if 'state' is the goal state (graduation).
        return state == self.goal_state
    
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

    def generate_actions(self, state):
        # Generate possible actions from 'state'.
        pass

    def transition(self, state, action):
        # Compute the next state based on 'action' from 'state'.
        pass

# Example usage:
if __name__ == "__main__":
    initial_state = "Freshman"
    goal_state = "Graduate"
    
    # Create an instance of A* search and run the search algorithm.
    search = AStarSearch(initial_state, goal_state)
    result = search.search()
    
    if result:
        print(f"Shortest path to graduation: {result}")
    else:
        print("No path to graduation found.")
