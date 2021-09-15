from BitStringGAProblem import BitChromosome
from TSPGAProblem import TSPChromosome
import random

### mixin for crossover.

class Crossover :
    def crossover(self, c1, c2) :
        raise NotImplementedError


### single-point bitstring crossover.
class OnePointStringCrossover(Crossover) :
    def crossover(self, c1, c2) :
        locus = random.randint(0,len(c1.bitstring) - 1)
        child1 = BitChromosome(c1.bitstring[:locus] + c2.bitstring[locus:])
        child2 = BitChromosome(c2.bitstring[:locus] + c1.bitstring[locus:])
        return child1, child2


### you do this one.

class TwoPointStringCrossover(Crossover) :
    def crossover(self, parent1, parent2) :

        return child1, child2


### for graph problems. You finish this one.
class PermutationCrossover(Crossover) :

    def crossover(self, parent1, parent2) :

        return child1, child2

## works with TSP Chromosomes.
### Assumes that a graph containing edge distances is set before crossover 
### is called. It should be named "edgegraph"

        
        

