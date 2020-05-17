# Escape Pods
# ===========

# You've blown up the LAMBCHOP doomsday device and broken the bunnies out of Lambda's prison - and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time. 

# Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

# Write a function solution(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

# For example, if you have:
# entrances = [0, 1]
# exits = [4, 5]
# path = [
#   [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
#   [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
#   [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
#   [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
#   [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
#   [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
# ]

# Then in each time step, the following might happen:
# 0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
# 1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
# 2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
# 3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

# So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.  (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final solution remains the same.)

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution({0, 1}, {4, 5}, {{0, 0, 4, 6, 0, 0}, {0, 0, 5, 2, 0, 0}, {0, 0, 0, 0, 4, 4}, {0, 0, 0, 0, 6, 6}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
# Output:
#     16

# Input:
# Solution.solution({0}, {3}, {{0, 7, 0, 0}, {0, 0, 6, 0}, {0, 0, 0, 8}, {9, 0, 0, 0}})
# Output:
#     6

# -- Python cases --
# Input:
# solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
# Output:
#     6

# Input:
# solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# Output:
#     16

from collections import deque
INF = float("inf")
class Graph:
    def __init__(self, entrances, exits, path):
        self.graph = [list(row) for row in path]
        self.nodes_number = len(self.graph)
        self.max_flow = None
        self.entrance = self.nodes_number
        self.exit = self.nodes_number + 1
        for row in xrange(self.nodes_number):
            self.graph[row].append(0)
            self.graph[row].append(INF if row in exits else 0)
        self.nodes_number += 2
        self.graph.append([(INF if x in entrances else 0) for x in xrange(self.nodes_number)])
        self.graph.append([0] * self.nodes_number)
    def bfs(self):
        visited = set()
        deq = deque()
        deq.append((self.entrance, [self.entrance]))
        while len(deq) > 0:
            current, path = deq.popleft()
            if current == self.exit:
                return path
            for i in xrange(self.nodes_number):
                if i not in visited and self.graph[current][i] > 0:
                    visited.add(i)
                    new_path = list(path)
                    new_path.append(i)
                    deq.append((i, new_path))
        return None
    def get_max_flow(self):
        if self.max_flow is None:
            max_flow = 0
            while True:
                shortest_path = self.bfs()
                if shortest_path is None:
                    break
                flow = INF
                for i in xrange(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    flow = min(flow, self.graph[node_from][node_to])
                for i in xrange(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    self.graph[node_from][node_to] -= flow
                    self.graph[node_to][node_from] += flow
                max_flow += flow
            self.max_flow = max_flow
        return self.max_flow
def solution(entrances, exits, path):
    g = Graph(entrances, exits, path)
    return g.get_max_flow()