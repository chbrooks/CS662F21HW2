### Homework 2: Genetic Algorithms.

#### due Sept 27 at the start of class.

For this problem, you will work with partially-completed code for a genetic algorithm, adding crossover, selection and mutation operators. You will also implement constraints for a scheduling
problem and evaluate the effectiveness of these operators and the difficulty of the corresponding problems. While there is not a lot of code to write for this assignment, doing this analysis may take you some time.

#### About the code

This code demonstrates a programming technique known as "mixins". This should be familiar to you if you've used Lisp or Scheme; Java's interface system is somewhat similar.
  
Mixins take advantage of Python's support for multiple inheritance to "mix in" behavior from several unrelated classes.
In our case, we'll use it to deal with one of the common frustrations involving GAs: all the different choices for implementing the algorithm.
    
We will mix in behavior from four different classes:

- GA. This is the class that performs the actual algorithm. It has an __init__ method, and a run() method which runs the GA. 
- Selector. This is the class that governs selection. It has a selectChromosomes method that takes a population as input and returns two individuals to act as parents. It is subclassed by TournamentSelector and RouletteSelector.
- Elitism. This is the class that governs elitism (retention of individuals from one generation to the next.) It implements one method: ApplyElitism, which take a population and an elitism rate
and returns a list of individuals to be kept for the next generation. It is subclassed by DeterministicElitism, TournamentElitism, and RouletteElitism. 
- Crossover. This is the class that governs the generation of new individuals. It implements one method: crossover, which takes
as input two parents and returns two children. It is subclassed by
OnePointStringCrossover, TwoPointStringCrossover, and PermutationCrossover.
- We also need a class to contain the problem knowledge, which includes a fitness function, a method to generate an initial population, and a method to mutate chromosomes. I have provided
three of these, along with an abstract base class.

  - BitStringGAProblem contains all of the information needed
     to solve a "bitstring" style GA problem. Its constructor takes as
     input a function to be used for fitness, and the length of each
     string in the population.

  - TSPGAProblem contains all of the information needed to
     construct and solve TSP-style problems. Its constructor takes as
     input a fitness function (I've provided one you might want to start with called
     computeTourCost) and the number of cities to work with. I've also provided a simplified version of graph.py that uses integers as vertices in the adjacency list.

  - NurseGAProblem contains the information needed to construct
   and evaluate the nurse scheduling problem. You will add additional constraints to make the problem more challenging.
    
This architecture may seem complicated, but it allows us to easily try out different combinations of elitism, crossover and selection mechanisms without editing, recompiling, or generating config
files. Instead, we create a mixin that inherits the specific classes whose behavior we want to incorporate. 

You are welcome to change the code to improve readability or add features or tests, but please do not modify the 
overall architecture.


**Part 1: (20 points)** start by working with the BitString problem.

Let's suppose we want to solve the "all-ones" problem: find a bitstring with all ones in it. This is easy, but will help us get going.

We start by making a fitness function:
<pre>
>>> def allOnes(chr) :
     return len([x for x in chr.bitstring if x == '1'])
</pre>

Now, we create a BitStringProblem. Let's suppose we want each
individual to be of length 20. We provide a fitness function and a length. Note that if we want to solve a different problem, we just provide a different fitness function.

<pre>
import BitStringGAProblem
b = BitStringGAProblem.BitStringGAProblem(allOnes,20)
</pre>
Lastly, we build a solver for this problem. Let's suppose we want to
use deterministic elitism, single-point crossover, and roulette selection. We would do:

<pre>
>>> class mySolver(GA.GA, Elitism.DeterministicElites, Crossover.OnePointStringCrossover, Selector.RouletteSelector):
...     pass
</pre>

This creates a class called mySolver that "mixes in" the behavior we
want. We then create an instance of this class, pass it the problem we
want to solve, and run it.
<pre>
>>> m=mySolver(b)
>>> m.run()
(output omitted)
</pre>
Run contains a number of optional arguments:
<ul>
  <li> popsize. How many individuals are in the population. </li>
  <li> elitismRate. The fraction of individuals carried over to the
  next generation without crossover. </li>
  <li> mutationRate. The probability that a child will undergo
  mutation. </li>
  <li> itersToRun.  How long the GA should run.  </li>
</ul>

There are three methods that you need to implement here:
- TournamentSelection
- Two-point Bitstring crossover
- RouletteElitism

(note: later on you'll compare these, so set up your test harness as you go.)

Then, implement the following fitness functions.
- even parity. (the string has an even number of 1s in it.)
- pattern. (the user provides a pattern, such as 10100010, and the fitness is the number of places where the bitstring matches the pattern.)
- treat the bitstring as a binary number and optimize -x^2 + 10x + 5.


**Part 2 (20 points):** solve the TSP problem.

- Recall the traveling salesman problem: Given a list of cities numbered
  0..n, with routes between each city, find the minimum tour that
  visits each city exactly once and returns to the start. 

We'll solve this with the TSPGAProblem class, which contains a TSPChromosome that stores the tours as lists of integers. I've also provided a simplified graph class that can
  generate random TSP problems.

You need to:
- implement PermutationCrossover
- adapt the TourCost fitness function to maximize rather than minimize.



**Part 3: (30 points)** The Nurse Scheduling Problem.

The problem can be stated as this: given a set of nurses n1 - nk, a
set of shifts s1-sj, and a set of constraints c1-cm, find an
assignment of nurses to shifts such that all constraints are
satisfied. (Or, if this is impossible, such that the constraints are
minimally violated.)
<br /><br />
We can represent the nurse scheduling problem as a matrix, with nurses
on the rows and shifts on the columns. A one in a cell in the matrix
indicates that the nurse is scheduled for that shift, and a 0
indicates he/she is not.  

for example:
<pre>
    s1    s2    s3
n1  0      1     1
n2  1      0     0
n3  0      1     0
    
</pre>
We can encode this as the bitstring 011101010.
<br /><br />

To begin, run the GA with the nursing problem on a simple example to
get the feel of it. I've provided you with two sample constraints:
oneNursePerShift, which says that each shift should have exactly one
nurse working it, and oneShiftEach, which says that each nurse should
work exactly one shift. (for there to be a solution, there must be the
same number of nurses as shifts). 
<br />
We can run this like so:
<pre>
>>> import ga
>>> import nurseFitness
>>> n=nurseFitness.nurseProblem(5,5)
>>> n.addConstraint(nurseFitness.oneNursePerShift)
>>> n.addConstraint(nurseFitness.oneShiftEach)
>>> g=ga.GA(nurseFitness.nurseFitness, 20, 100, 0.1, 26, 0.1, n)
>>> g.runGA()
</pre>
This will create a nurseProblem with 5 nurses and 5 shifts, attach the
two constraints, and then run the GA with a population of 20
individuals for 100 iterations, with elitism and mutationRate of 0.1
and a string length of 26.

Your job is to code some more interesting constraints for a larger
problem. Here are the parameters:

We want to staff a floor on a hospital for a one-week schedule. The
hospital has three 8-hour shifts per day, 7 days a week, for a total
of 21 shifts. There are 10 nurses who work on the floor.

add the following constraints:
- There must be at least one nurse, and at most three nurses, on
  each shift.
- Each nurse should be scheduled for five shifts per week.
- No nurse can work more than three days in a row without a day
  off.
- Nurses prefer consistency - they would like to always work the
  same shift (days, evenings, or nights).

You should write constraint functions for each of these
constraints. These functions should return (0-number of constraints
violated). For example,

- a schedule with one nurse working 6 shifts, and one working 4,
  and all others working 5, would return -2 when evaluated by the
  fiveShiftsPerNurse constraint.
- A schedule with a nurse working 3 day shifts and 2 night shifts
  would return -2 when evaluated by the consistency constraint.</li>

You will want to test each of these constraints separately.

**Part 4: (30 points)** Summary.

For each of the three problems, we would like to understand how our choice of selection, mutation, crossover and elitism affects performance, which can mean the quality of the solution we find and the time needed to find it. 

I would like you to prepare a report, in Word or PDF format, that contains at least three experiments for each type of problem (bitstring, TSP, NurseScheduling). You can choose what paramters you want to consider; you might want to consider problem difficulty, or compare selection strategies, or high vs low mutation rates, or the effect of elitism. Find a phenomenon that you think is interesting.

For each experiment, prepare a plot, figure or table that illustrates the result of the experiment, along with a description of the experiment and (especially!) what the conclusions are. That is, don't just say what the experiment was, explain the result!

Please include this in your repo along with your code.

