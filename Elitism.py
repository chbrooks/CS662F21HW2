import random
### we'll use the 'mixin' style here.

class Elites :

    def ApplyElitism(self, pop, erate) :
        raise NotImplementedError


class DeterministicElites(Elites) :
    def ApplyElitism(self, pop, erate) :
        pop.sort()
        pop.reverse()
        return pop[0:int(erate*len(pop))]

class TournamentElites(Elites) :
    def ApplyElitism(self, pop, erate) :
        children = []
        for i in range(int(erate * len(pop))) :
            c1 = random.choice(pop)
            c2 = random.choice(pop)
            if c1 > c2 :
                children.append(c1)
            else :
                children.append(c2)
        return children

## you do this one. pop is the current population, erate is the fraction to retain

class RouletteElites(Elites) :
    def ApplyElitism(self, pop, erate) :

        return children


            
