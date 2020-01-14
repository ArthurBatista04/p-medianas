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


def tournament(population):
    number = int(n/10)
    for i in number:
        indiviual = random.uniform(0, n)
