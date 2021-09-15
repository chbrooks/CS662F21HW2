### simpler adjacency list. Mapping integers to lists of edges.
import random

class Edge() :
    def __init__(self, src,dest, weight) :
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self) :
        return "(%d, %d, %d)" % (self.src, self.dest, self.weight)


### keys in the edgeMap are integers. The values are lists of edges.
class Graph() :
    def __init__(self):
        self.edgeMap = {}

    ### implements the 'in' keyword. Returns true if the node is in the graph.
    def __contains__(self, item):
        return item in self.edgeMap

    def __repr__(self):
        return " ".join([str(x) for x in self.edgeMap])

    def addEdge(self, src, dest, weight):
        e = Edge(src, dest, weight)
        if src in self.edgeMap:
            self.edgeMap[src].append(e)
        else:
            self.edgeMap[src] = [e]

    ## src is an int. Look up the node in the NodeTable and use that to fetch the edges.
    def getEdges(self, src):
        return self.edgeMap[src]


def makeTSPGraph(ncities) :
    g = Graph()
    for i in range(ncities) :
        for j in range(i + 1, ncities) :
            if i != j :
                weight = random.randint(1, 50)
                g.addEdge(i,j,weight)
                g.addEdge(j,i,weight)
    return g


def tourCost(inputGraph, tour) :
    cost = 0
    for i in range(len(tour) - 1):
        edges = inputGraph.getEdges(tour[i])
        for edge in edges:
            if edge.dest == tour[i + 1]:
                cost += edge.weight
        ## not checking for unreachable, or multiple edges
    edges = inputGraph.getEdges(tour[-1])
    for edge in edges:
        if edge.dest == tour[0]:
            cost += edge.weight
    return cost
