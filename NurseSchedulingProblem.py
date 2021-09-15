from GAProblem import GAProblem, Chromosome
from BitStringGAProblem import BitStringGAProblem
import random

### we can represent the nurse scheduling problem as a matrix, with nurses on 
### the rows and shifts on the columns. A one in a cell in the matrix indicates
### that the nurse is scheduled for that shift, and a 0 indicates he/she is 
### not. 

### for example:
###      s1    s2    s3
###  n1  0      1     1
###  n2  1      0     0
###  n3  0      1     0

### we can encode this as the bitstring 011101110 

### We can use the regular BitStringProblem class to represent Nurse Scheduling problems. We 
### just need a factory that can produce appropriate fitness functions, given a set of constraints. 
### note an interesting Python trick - we are storing a list of functions that we can evaluate dynamically.

## given a list of constraints, return a function that takes all of them and computes their sum.
## constraints are negative values, so let's add 100

def NurseFactory(constraints) :
    def f(chr) :
        return 100 + sum([constraint(chr)
               for constraint in constraints])
    return f


class nurseSchedulingProblem(BitStringGAProblem) :

    def __init__(self, nnurses=3, nshifts=3, constraints=[], printfn = None) :
        self.nurses = nnurses
        self.shifts = nshifts
        self.constraints = constraints
        self.fitnessFn = NurseFactory(self.constraints)
        self.strlength = nnurses * nshifts
        self.printfn = printfn
        BitStringGAProblem.__init__(self, self.fitnessFn, self.strlength)

    def addConstraint(self, constr) :
        self.constraints.append(constr)
        self.fitnessFn =NurseFactory(self.constraints)


### Now we just need to build constraints that let us describe different schedules. Here's a couple to get you started.
### Let's assume three shifts per day, seven days per week, and three nurses. 
### This means our biststring is of length 3 * 7 * 3=63
numNurses = 3
numShifts = 3
numDays = 7

### a constraint: each nurse should work exactly 1 shift. 
def oneShiftEach(chromosome) :
    daylen = numShifts * numDays
    total = 0
    for i in range(numNurses) :
        total -= abs(1 - chromosome.bitstring[i*daylen:(i+1)*daylen].count('1'))
    return total

### There should be exactly one nurse working each shift.
def oneNursePerShift(chromosome) :
    ### convert the bitstring into a list of lists, one per shift, with 
    shiftlist = getShifts(chromosome.bitstring)
    return -1 * sum([abs(shift.count('1') - 1) for shift in shiftlist])

### return a list of lists, one for each nurse's schedule
def getShifts(bitstring) :
    nlist = []
    for i in range(numShifts) :
        shift = []
        for j in range(numNurses) :
            shift.append(bitstring[(j*numShifts) +i])
        nlist.append(shift)
    return nlist

