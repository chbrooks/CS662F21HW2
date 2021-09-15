import random
class Selector :
    
    ### given a population, choose two parents
    def selectChromosomes(self, pop) :
        raise NotImplementedError

### you do this one.

class TournamentSelector(Selector) :
    def selectChromosomes(self, pop) :

        return child1,child2

### choose two parents via roulette selection
class RouletteSelector(Selector) :
    def selectChromosomes(self, pop) :
        total = sum([x.fitness for x in pop])
        rval = random.randint(0,total)
        i = 0
        counter = pop[0].fitness
        while counter < rval and i < len(pop) -1:
            counter += pop[i].fitness
            i += 1
        c1 = pop[i]
        rval = random.randint(0,total)
        i = 0
        counter = pop[0].fitness
        while counter < rval and i < len(pop) -1:
            counter += pop[i].fitness
            i += 1
        c2 = pop[i]
        return c1,c2
