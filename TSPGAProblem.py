from GAProblem import GAProblem, Chromosome
import random

### How to use this:
### 1. Create a graph. You can either generate a random one or read it in from a file.
### import buildGraph, TSPGAProblem
### g = graph.makeTSPGraph(4)

### 2. Create a fitness function. graph.py has a tourcost. You should change that so that fitter solutions
### have higher values.


### 3. Create a TSPGAProblem.
### newProblem = TSPGAProblem(f, g)

### 4. Solve as before by creating a solver.


class TSPGAProblem(GAProblem) :

    ### g is a graph that will be used to represent the TSP
    def __init__(self, fitnessFn, g) :
        GAProblem.__init__(self, fitnessFn)
        self.g = g


    def makePopulation(self, popsize) :
        pop = []
        for i in range(popsize) :
            clist = self.g.adjlist.keys()
            random.shuffle(clist)
            pop.append(TSPChromosome(clist))
        return pop

    def evalFitness(self, pop) :
        for p in pop:
            p.fitness = self.fitnessFn(p)

    def solved(self,pop) :
        return False

### Mutate will swap the position of two cities.
    def mutate(self, c) :
        c1 = random.randint(0,len(c.citylist) -1)
        c2 = random.randint(0,len(c.citylist) -1)
        c.citylist[c1], c.citylist[c2] = c.citylist[c2], c.citylist[c1]



### Assume that a citylist is a list of integers representing nodes in the graph.
### For example: [1,5,4,3,6,2]

class TSPChromosome(Chromosome) :
    def __init__(self, citylist) :
        Chromosome.__init__(self)
        self.citylist = citylist

    def __repr__(self) :
        return "%s %d" % (self.citylist, self.fitness)







