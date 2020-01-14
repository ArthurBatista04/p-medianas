from solution import Solution
from copy import deepcopy
import random
# number of solutions in population
n = 100


def generateRandomSample(genes, numVerties, numMedians):
    return [Solution(deepcopy(genes), int(numVerties), int(numMedians)) for i in range(n)]


def evaluate(population):
    for solution in population:
        solution.fitness()


def selection(population):
    picks = []
    k = 4
    for i in range(k):
        indice = int(random.uniform(0, n))
        picks.append(population[indice])
    max = picks[0]
    secondmax = picks[1]
    for i in range(2, k):
        if picks[i].fitness > max.fitness:
            secondmax = max
            max = picks[i]
        else:
            if picks[i].fitness > secondmax.fitness:
                secondmax = picks[i]
    return max, secondmax
