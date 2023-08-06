import heapq

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


def Bfs(self, start, end):

    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]  # Checks if last added node is the end node, otherwise continue loop
        if node == end:
            return path
        for adjacent in self.gdict.get(node, []):  # get fxn gets the node and adjacents
            new_path = list(path)  # constructs new path
            new_path.append(adjacent)  # appends new path to adjacent vertex
            queue.append(new_path)  # queues the appended to the new path


# BFS does NOT work with weighted graphs, because it may not look at all possible lowest-cost paths
# Works only for unweighted + undirected graphs, as well as unweighted + directed graphs

print('\n----------------------------------DIJKSTRA ALGORITHM SOLUTION---------------------------------------------\n')
# Optimization problem where we want to minimize the sum of the edges
# All edges initial value is INFINITY other than starting point 'A', start=0
# Consider all neighboring vertices from starting point
# We use heap as underlying structure b/c we can take minimum value in a constant running TC
# Afterwards we rearrange the heap DS which can be done in log TC

# Start by comparing edge wt with vertex value (lets say edge from A to B = 6, B vertex val = INFINITY)
# 6 < INF so B = 6
# Once you consider all possible neighbor vertices of A, label A as visited and heap should look like:
# HEAP : [ B-6, D-9, C-10 ]
# Lowest value is B-6, so remove from heap and continue w/ neighbors of B (compare edge wt vs. vertices)

# Calculate distance from B(6) to neighbors (+ edge wt) and compare to neighboring vertex values of INF)
# 6   13   INF
# B -----> F,                 6+13 = 19 < INF so F= 19

# After considering all neighbors of B, they are all inserted to the heap with their corresponding values
# Then we mark B as visited, and continue with the lowest value vertex within the heap

# When we implement, we keep predecessor of any vertex to indentify the vertex we came from to the new vertex

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")  # initializes inf value on nodes

    def __lt__(self, other_node):  # we use __lt__ (less than) to compare objects
        return self.min_distance < other_node.min_distance  # specify to compare min_distance of each node

    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)  # adds edge to the list of neighbors


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)  # inserts element to heap, order is adjusted to maintain min heap DS

        while self.heap:
            actual_vertex = heapq.heappop(self.heap)  # using min heap, guarantees smallest value will be popped
            if actual_vertex.visited:
                continue

            for edge in actual_vertex.neighbors:  # consider neighbors
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight  # calculates curr_min distance w/ edge wt
                # to find distance to target vertex
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start

                    heapq.heappush(self.heap, target)  # updates the heap

            actual_vertex.visited = True
    def get_shortest_path(self, vertex):
        print(f'Shortest path is: {vertex.min_distance}')
        actual_vertex = vertex

        while actual_vertex is not None:
            print(actual_vertex.name, end="")
            actual_vertex = actual_vertex.predecessor

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")

# Add values and edges arbitrarily
nodeA.add_edge(6, nodeB)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)

# HOWEVER, when it comes to negative cycles, Dijkstra does not work here (goes until infinity each run since negative)
# Thus, we resort to Bellman Ford Algorithm

print('\n-------------------------------BELLMAN FORD ALGORITHM SOLUTION-------------------------------------------\n')
# BFA addresses negative cycle issue, and works for all kinds of graphs (all 7 kinds)
# If a negative cycle is present, BFA reports it but does not actually find SSP
# We run iterations through a given edge V-1 times

# In Dijkstra we processed updating distance by using min heap property
# In BFA we process the edges as given (without any sorting)

# In BFA, if we are in the Vth iteration and the weights of the vertices change, this means negative cycle is present

# BFA tries to see if any node achieved the better distance in the previous iterations
# If better distance is achieved in the previous iteration, in current step, it tries to use that better distance
# and improve the distance of other vertices

# During each iteration, shortest path to each vertex is updated by considering all edges in the graph
# By repeating this V-1 times, we can guarantee that the shortest path to all vertices has been found, provided no
# negative wt cycles in the graph

# If we ran less than V-1 times, might miss finding the shortest path to some vertices in the graph
# Running BF for more than V-1 times however does not change the shortest path to any vertex and may lead to
# unnecessary computations. If wts change after V-1, implies neg. cycle

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s,d,w])

    def addNode(self, value):
        self.nodes.append(value)


    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print('' + key, ': ', value)

    def bellmanford(self, src):
        dist = {i:float("inf") for i in self.nodes}  # initializes dict, setting dict values to infinity
        dist[src] = 0  # we initialize through looping node list. If we have v nodes, takes O(v)

        for _ in range(self.v-1):  # now loop v-1 times, and in this loop, loop for edges
            for s,d,w in self.graph:  # if dist of source not inf and dist source + w less than dist of destination,
                if dist[s] != float("inf") and dist[s] + w < dist[d]:  # we update
                    dist[d] = dist[s] + w

            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist [d]:
                    print('Graph has negative cycle')
                    return

# 1) Get all distance to infinity except source (=0)
# 2) Run loop V-1 times, check if cond
# 3) Run Vth time w/ same if cond, and if it is true, negative cycle is present

print('\n---------------------------------------SSP TC and SC-----------------------------------------------------')
class Question:

    def ask_tc():
        ans= (input('What is the TC of this operation? Remove parenthesis and spaces from your answer')).upper()
        if ans[0] != 'O':
            print ('Please provide an answer in big O notation. Try again')
            Question.ask_tc()
        return ans

    def ask_sc():
        ans = (input('What is the SC of this operation? Remove parenthesis and spaces from your answer')).upper()
        if ans[0]  != 'O':
            print('Please provide an answer in big O notation. Try again')
            Question.ask_sc()
        return ans

    def ask_shoulduse():
        answers = ['Y', 'N']
        ans = str((input('Should we use arrays in this situation? Input y for yes and n for no (remove spaces)')).upper())
        if ans not in answers:
            print ('Please provide a valid input.')
            Question.ask_shoulduse()
        return ans

class SSP:

    tc_set = {'Breadth First Search': 'O(V^2)', 'Dijkstra Algorithm': 'O(V^2)', 'Bellman Ford Algorithm': 'O(EV)'}
    sc_set = {'Breadth First Search': 'O(E)', 'Dijkstra Algorithm': 'O(V)', 'Bellman Ford Algorithm': 'O(V)'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print ('Incorrect! From the beginning!')
                SSP.assess_tc(SSP.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        SSP.assess_sc(SSP.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                SSP.assess_sc(SSP.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')

SSP.assess_tc(SSP.tc_set)


additional = [['BFS', 'DIJKSTRA', 'BFA'],
              ['Easy', 'Moderate', 'Moderate'],
              ['Not for weighted graphs', 'Not for negative cycle graphs', 'Everything'],
              ['TC good, easy implement', 'Dont use, implementation hard', 'Dont use, TC bad'],
              ['Not supported', 'Use, TC is better than BFA', 'Dont use, TC bad'],
              ['Not supported', 'Not supported', 'Use, others dont account for it']]

print('\n BFS vs. DIJKSTRA vs. BFA\n'
      f'\n                 {additional[0]}'
      f'\n Implementation: {additional[1]}'
      f'\n Limitations: {additional[2]}'
      f'\n Unweighted Graphs: {additional[3]}'
      f'\n Weighted Graphs: {additional[4]}'
      f'\n Negative Cycle: {additional[5]}')






















