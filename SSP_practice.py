print('----------------------------------SINGLE SHORTEST PATH-----------------------------------------------\n')
# Consists of finding a path from a given vertex (the source) to all other vertices in the graph where distance is min

# 3 solutions:
# 1) Breadth First Search (BFS)
# 2) Dijsktra's Algorithm
# 3) Bellman Ford Algorithm

print('\n----------------------------------BFS SOLUTION-----------------------------------------------\n')
# Logic:
# - Enqueue any starting vertex
# - While queue is not empty:
# - P = Dequeue()
# - if P is unvisited: mark as visited, enqueue adjacent unvisited vertices of p, update parent of adjacent vert to
# the current vertex

