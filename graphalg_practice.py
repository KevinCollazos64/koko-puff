print('\n---------------------GRAPH ALGORITHMS--------------------------\n')
# graphs are nonlinear data structures consisting of nodes (or vertices) and edges (connects nodes)
# Need graphs for single shortest path problems and of the like

print('\n TERMINOLOGY:'
      '\n Vertices - Nodes of the graph'
      '\n Edge - Lines that connects pair of vertices'
      '\n Unweighted graph - Graph which does not have weight associated w/ any edge'
      '\n Weighted graph - Graph which has weight associated w/ any edge'
      '\n Undirected graph - Edges of graph w/ no direction associated w/ them'
      '\n Directed graph - If edges have an associated direction'
      '\n Cycle graph - Graph w/ at least one loop (one cycle)'
      '\n Acyclic graph - Graph w/ no loops'
      '\n Tree - Special case of directed acyclic graph')

print('\n GRAPH TYPES:'
      '\n 1) UNWEIGHTED - UNDIRECTED (no direction, so you can go back and forth + no associated wt'
      '\n 2) UNWEIGHTED - DIRECTED (You can only go in that direction + no associated wt'
      '\n 3) POSITIVE - WEIGHTED - UNDIRECTED (No direction, only positive #s associated w/ edges)'
      '\n 4) POSITIVE - WEIGHTED - DIRECTED (Direction + only positive weights)'
      '\n 5) NEGATIVE - WEIGHTED - UNDIRECTED (If there is at least ONE wt w/ negative value, entire'
      'graph is negative. No direction so you can move in any way + weights (at least one negative)'
      '\n 6) NEGATIVE - WEIGHTED - DIRECTED (Direction so you can only move one way + negative values')


print ('\n GRAPH REPRESENTATIONS:'
       '\n1) Adjacency Matrix: A square matrix (2d array) & elements of the matrix indicate whether pairs'
       '\n of vertices are adjacent or not in the graph'
       '\n2) Adjacency List: Collection of unordered lists used to represent a graph. Each list describes'
       '\n the set of neighbors of a vertex in the graph (Stores vertices in array, edges in Linked List')


# A complete graph is one /w the maximum number of edges within the graph.

# If a graph is complete or almost complete you should use Adjacency Matrix (all cells of square matrix filled)
# If number of edges are few, then we should use Adjacency List

# We can also use dictionaries for adjacency lists, where keys are the vertices from the graph and the edges will
# be represented as values in the keys inside list

print('\n---------------------CREATING GRAPH--------------------------\n')
# Initialize dict


class Graph:
    def __init__(self, gdict= None):  # Constructor
        if gdict is None:
            gdict = {}  # Creates adjacency list
        self.gdict = gdict


# Create fxn for adding edges
    def add_edge(self, v1, v2):
        if v1 in self.gdict.keys() and v2 in self.gdict.keys():
            self.gdict[v1].append(v2)
            self.gdict[v2].append(v1)
            return True
        return False



# Add vertex class
    def add_vertex(self, vertex):  # Adds the vertex like this:
        if vertex not in self.gdict.keys():  # {
            self.gdict[vertex] = []  #               A: []
            return True  #                      }
        return False  # To connect vertices it would look like A[B] etc

# Remove edge fxn

    def remove_edge(self, v1, v2):
        if v1 in self.gdict.keys() and v2 in self.gdict.keys():
            try:
                self.gdict[v1].remove(v2)
                self.gdict[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

# Remove vertex fxn

    def removevertex(self, v):
        if v in self.gdict.keys():
            for other_v in self.gdict[v]:
                self.gdict[other_v].remove(v)
            del self.gdict[v]
            return True
        return False

    def bfs(self, v):  # You can apply BFS to any type of graph
        visited = [v]
        queue = [v]
        while queue:
            deVertex = queue.pop()
            print(deVertex)
            for adjacentvertex in self.gdict[deVertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)

    def dfs(self, v):
        visited = [v]
        stack = [v]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentvertex in self.gdict[popVertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    stack.append(adjacentvertex)


print('\n---------------------GRAPH TRAVERSAL--------------------------\n')
# BREADTH FIRST search vs. DEPTH FIRST search

# BFS : Start at arbitrary node, explores neighbor nodes at same level before moving to next level

# Enqueue any start vertex
# While queue is not empty:
# P = dequeue()
# if P is unvisited, mark it as visited
# Enqueue all adjacent unvisited vertices of P


# DFS : Start at random node, explore as far as possible along each edge before backtracking

# Push starting vertex to stack
# While stack is not empty:
# P = pop()
# if P is unvisited:
# Mark as visited
# Push all adjacent unvisited vertices of P

print('\n---------------------TOPOLOGICAL SORT--------------------------\n')
# Sorts given actions in a way that identifies dependencies
# For ex: If action 2 depends on action 1, action 2 will always come after parent action 1
# Another ex: Exercise -> Bath -> Breakfast. Can't have breakfast without making it, and can't make it without buying

# If a vertex depends on current Vertex:
# GO to the vertex and then come back to current Vertex
# Else
# Push currentVertex to stack

# There is naturally v number of solutions where v is the number of vertices
# The solution we come to depends on the vertex we start at

from collections import defaultdict

class Graph2:
    def __init__(self, numVertices):
        self.graph = defaultdict(list)
        self.numVertices = numVertices

    def addEdge(self, v, e):
        self.graph[v].append(e)

    def toposortutil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.toposortutil(i, visited, stack)

        stack.insert(0, v)

    def toposort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.toposortutil(k, visited, stack)

        print(stack)

print('\n---------------------TC AND SC OF GRAPHING ALGORITHMS AND OPERATIONS--------------------------\n')

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


class GA_set:

    tc_set = {'Breadth first search': 'OV+E', 'Depth first search': 'OV+E', 'Topological sort': 'OV+E',
              'Internal Data structure of BFS': 'Queue', 'Internal Data structure of DFS': 'Stack'}

    sc_set = {'Breadth first search': 'OV+E', 'Depth first search': 'OV+E', 'Topological sort': 'OV+E'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                GA_set.assess_tc(GA_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        GA_set.assess_sc(GA_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                GA_set.assess_sc(GA_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


GA_set.assess_tc(GA_set.tc_set)

# We use BFS if target is close to starting point
# Else, we use DFS if target is buried deep




