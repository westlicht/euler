#!/usr/bin/python

import heapq
from collections import defaultdict

class PathFind(object):
    def __init__(self):
        self.G = defaultdict(dict)
        self.E = defaultdict(dict)
    def addEdge(self, va, vb, cost, edge, way):
        if way == -1: (vb, va) = (va, vb)
        self.G[va][vb] = edge
        if not way: self.G[vb][va] = edge
        self.E[edge] = cost

    def findPath(self, start, end):
       def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
         while len(L) > 0:
           yield L[0]
           L = L[1]

       q = [(0, start, ())]  # Heap of (cost, path_head, path_rest).
       visited = set()       # Visited vertices.

       # Eliminate the dots pattern
       push, pop, add = heapq.heappush, heapq.heappop, visited.add
       G, E = self.G, self.E

       while True:
          (cost, v1, path) = pop(q)
          if v1 not in visited:
             add(v1)
             path = (v1, path)

             if v1 == end: return list(flatten(path))[::-1]

             for (v2, e) in G[v1].iteritems():
                 if v2 not in visited:
                   push(q, (cost + E[e], v2, path))

    def getEdges(self, path):
        edges = []
        for ix in xrange(len(path) - 1):
            edges.append(self.G[path[ix]][path[ix + 1]])
        return edges

class Node(object):
	def __init__(self, value):
		self.value = value

	def getValue(self):
		return self.value

class Edge(object):
	def __init__(self, a, b):
		pass

def loadfile(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close

	rows = []
	for line in lines:
		row = []
		values = line.split(" ")
		for value in values:
			row.append(Node(int(value)))
		rows.append(row)

	return rows
		
def find():
	rows = loadfile("input2.txt")

	pf = PathFind()

	for i in range(0,len(rows)-1,1):
		row1 = rows[i]
		row2 = rows[i + 1]
		for j in range(len(row1)):
			a = row1[j]
			b1 = row2[j]
			b2 = row2[j + 1]
			edge1 = Edge(a, b1)
			edge2 = Edge(a, b2)
			cost1 = 100 - b1.getValue()
			cost2 = 100 - b2.getValue()
			pf.addEdge(a, b1, cost1, edge1, 1)
			pf.addEdge(a, b2, cost2, edge2, 1)

	start = rows[0][0]
	goal = Node(0)
	for j in range(len(row2)):
		a = row2[j]
		edge = Edge(a, goal)
		pf.addEdge(a, goal, 0, edge, 1)
	
	path = pf.findPath(start, goal)
	sum = 0
	for item in path:
		print item.getValue()
		sum += item.getValue()

	return sum


print find()
