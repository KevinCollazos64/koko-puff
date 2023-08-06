print('----------------------------------ALL PAIRS SHORTEST PATH-----------------------------------------------\n')

# We find the shortest path from ALL vertices (all vertices are treated as source vertex) and use any SSP alg for each

print('----------------------------------FLOYD WALSH ALGORITHM-----------------------------------------------\n')
# First step is to create a matrix with vertices, edges and their values ( 0 - source and destination are the same,
# "inf" indicates we don't know if there is a path between these vertices or not )
# In FWA, we keep updating cells in the matrix until we find the shortest path of all the vertices


# If D[u][v] > D[u][viax] + D[viax][u] :
#     D[u][v] = D[u][viax] + D[viax][x]

# D = distance  u = source vertex
# v = destination vertex  viax = destination vertex
# If the dstance between 2 vertices greater than distance between source vertex via x + distance between via x to
# destination vertex, we update the distance

# Repeat iteration as many times as there are vertices
# Try all vertices as viax, one for each iteration

print('\nWhy do we need it?\n'
      'In every iteration, we improve paths between nodes\n'
      '\nThere are 3 possible ways to find distance between a source and vertex:'
      '\n 1) Vertex not reachable (vertex has no edges connecting it  - If this is present, no point in running FWA'
      '\n 2) 2 vertices directly connected  - In this case, FWA is the best solution'
      '\n 3) 2 vertices are connected via other vertex\n'
      '\nAll viable cases are taken into account in the case of FWA (by iterating through all nodes can always be'
      '\nguaranteed that FWA answer is the correct one')

print('\nFWA however does not work with negative cycles...'
      '\nTo go through cycle we need to go via negative cycle participating vertex at least twice'
      '\nFWA never runs loop twice and therefore does not run through the same vertex'
      '\nHence, FWA can never detect a negative cycle')

def FloydWalshalg(nv, G):
    distance = G  # initialize graph to another graph, so we can change values. We want to keep initial version of graph
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):  # need to run loop such that we visit each cell in 2D array in FWA
                # to do so we need to run nested loop inside each other: one for rows, one for columns
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                # if direct distance > distance via some other vertex, we take distance via other vertex


G = [[0, 8, "inf", 1],
     ["inf", 0, 1, "inf"],
     [4, "inf", 0, "inf"],
     ["inf", 2, 9, 1]]


print('\nThe time complexity for FWA is O(V**3) where V is the number of vertices'
      '\nThe space complexity is O(V**2)\n')

additional = [['BFS', 'DIJKSTRA', 'BFA', 'FWA'],
              ['Easy', 'Moderate', 'Moderate', 'Moderate'],
              ['Not for weighted graphs', 'Not for negative cycle graphs', 'Everything', 'Not for negative cycle'],
              ['TC good, easy implement', 'Dont use, implementation hard', 'Dont use, TC bad', 'Can use'],
              ['Not supported', 'Use, TC is better than BFA', 'Dont use, TC bad', 'Use, implementation easy'],
              ['Not supported', 'Not supported', 'Use, others dont account for it', 'Not supported']]

print('\n BFS vs. DIJKSTRA vs. BFA vs. FWA\n'
      f'\n                 {additional[0]}'
      f'\n Implementation: {additional[1]}'
      f'\n Limitations: {additional[2]}'
      f'\n Unweighted Graphs: {additional[3]}'
      f'\n Weighted Graphs: {additional[4]}'
      f'\n Negative Cycle: {additional[5]}')
