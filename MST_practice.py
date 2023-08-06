import sys

print('----------------------------------MINIMUM SPANNING TREE-----------------------------------------------\n')

print('MST is a subset of edges of connected, weighted and undirected graph which:'
     '\n- Connects all vertices together'
     '\n- No Cycle'
     '\n- Minimum total edge')


# IRL example: Asked to connect five islands with bridges
# Cost of bridges between island varies based on different  factors
# Which bridge should be constructed such that all islands are accessible and cost is minimum?

# In SSSP we take one island as a source and find cheapest way from this island
# SSSP : Take source and find cheapest way from this source

# In MST we don't take any island as a source island, and we are not finding minimum path from any of the islands
# we simply find the minimum cost
# MST : The cheapest way of connecting all vertices

print('\n----------------------------------DISJOINT SET-----------------------------------------------\n')
print('\nWe will use this in our MST algorithms'
      '\nDisjoint set is a data structure that keeps track of set of elements partitioned into number of disjoint'
      '\nand non overlapping sets and each set has a representative which helps in identifying that set')


# Disjoint sets have no element in common
# Each set is represented by 1 element

# Makeset(N) - used to create initial set where n is number of elements
# Union(x,y) - merge two given sets
# findset(x) - returns the set name in which this element is present


class Disjointset:
    def __init__(self, vertices):  # initialize vertices, parent (to identify set of vertex), ranks
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v  # initializing the parents of the vertices to itself
        self.rank = dict.fromkeys(vertices, 0)  # We create dict based on vertices, we set rank for it. We use rank
        # inside the union, when we union the set and set the parent

    def find(self, item):  # return parent of set of this other set, so we increase the root
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:  # if you join 2 sets same rank, else cond. sets the first set as
            self.parent[yroot] = xroot  # parent of the second

        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1  # increase rank b/c xroot is the parent of yroot now


print('\n---------------------------------Kruskals Algorithm-----------------------------------------------\n')
# This is a greedy algorithm where we try to find the best solution in each step
# Finds MST for weighted undirected graph in 2 ways:
#  1) Add increasing cost edges at each step
#  2) Avoid any cycle at each stage

# PSEUDOCODE:
# For each vertex:
#   makeset(v)
# sort each edge in non decreasing order by weight
# for each edge (u, v):
#   if findset(u) != findset(v):
#       union (u,v)
#       cost = cost + edge(u,v)

# We create each vertex as a set
# Sort the edges
# For each edge we check if edge parent does not equal, then we unionize them and set new cost

# TC: O(elog(E)) where E is the edges
# SC: O(V+E)


def kruskalalgo(self):  # no parameters becasue no source vertex
    i, e = 0,0
    ds = Disjointset(self.nodes)  # creates set for each node, sets parents to themselves, and rank = 0 for all nodes
    self.graph = sorted(self.graph, key=lambda item: item[2])  # sorts the edges in our graph
    while e < self.v - 1:  # v-1 b/c index starts at 0
        s, d, w = self.graph[i]  # inside graph list we re-store the edge
        i += 1
        x = ds.find(s)
        y = ds.find(d)
        if x != y:  # if they don't belong to the same set
            e += 1
            self.MST.append([s, d, w])
            ds.union(x, y)



print('\n---------------------------------Prims Algorithm-----------------------------------------------\n')
# Another greedy algorithm
# Finds the MST for weighted, undirected graph through:
#  1) Take any vertex as source, set its weight to 0, and over vertices = "inf"
#  2) For every adjacent vertices, if current wt > current edge, then we set it to current edge
#  3) Mark current vertex as visited
#  4) Repeat these steps for all vertices in increasing order of weight

# import sys
class Graph:
    def __init__(self, vertexnum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexnum = vertexnum
        self.MST = []

    def printsolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))


    def primsalgo(self):  # create array that keeps list of visisted nodes
        visited = [0] * self.vertexnum  # [0] means none are visited
        edgenum = 0  # b/c we start from 0 to explore unvisited nodes
        visited[0] = True

        while edgenum < self.vertexnum -1:  # -1 b/c index starts from 0
            min = sys.maxsize
            for i in range(self.vertexnum):  # if node is visited, then we will check for adjacent vertices, while
                if visited[i]:  # we do that we check if it is not visited, and there's an edge, we will find the
                    for j in range(self.vertexnum):  # min cycle
                        if (not visited[j]) and self.edges[i][j]:
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgenum += 1  # b/c we have to visit all edges

#  TC : O(V **3) b/c 3 nested loops, but if we use adjacency list, TC for prims alg can be O(ElogV)
#  SC : O(V) b/c we insert V number of vertices to our MST


edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]

nodes = ["A", "B", "C", "D", "E"]
samp = Graph(5, edges, nodes)
samp.primsalgo()

print('\n---------------------------------KRUSKAL VS. PRIMS-----------------------------------------------\n')

print('\nKRUSKAL:\n'
      '- concentrates on edges\n'
      '- Finalize edge in each iteration\n'
      '- Selects the minimum edge as the best solution in the current stage\n'
      '- Everytime when we select edge, we check that we dont have any cycle (what we try to avoid)')

print('\nPRIMS:\n'
      '- concentrates on vertices\n'
      '- Finalize a vertex in each iteration\n'
      '- Start with arbitrary vertex then continues w/ the vertex w/ min wt\n'
      '- continues to other adjacent vertices w/ best solution where wt is min')



