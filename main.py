from copy import deepcopy
import random
from math import inf
import sys
n = 100  # number of population


class Vertice(object):
    def __init__(self, x, y, cap, demand):
        self.x = x
        self.y = y
        self.cap = cap - demand
        self.demand = demand
        self.id = random.random()


class Individual(object):
    def __init__(medians, fitness):
        self.medians = medians
        self.fitness = fitness
        self.newIndivual = True


def inputParse(input):
    lines = []
    vertices, medians = input.pop(0).split()
    for eachLine in input:
        x, y, cap, demand = eachLine.split()
        vertice = Vertice(int(x), int(y), int(cap), int(demand))
        lines.append(vertice)
    return [lines, vertices, medians]


def generateRandomSolution(genes, numVertices, numMedians):
    # Generates a random solution of medianas vertices
    count = 0
    solution = {}
    for i in range(numMedians):
        count += 1
        rand = random.randint(0, numVertices-count)
        candidate = genes.pop(rand)
        solution[candidate.id] = candidate
    return [solution, genes]


def generateRandomPopulation(n, genes, numVerties, numMedians):
    return [generateRandomSolution(deepcopy(genes), int(numVerties), int(numMedians)) for i in range(n)]


def distance(x, x0, y, y0): return ((x-x0)**2 + (y-y0)**2)**0.5


def neighborhoodDistance(solution, population):
    # find the neartes neighbors to the medians and calculate there distance
    distances = {median: 0 for median in solution}
    for individual in population:
        minNodes = {'value': inf}
        for medianId in solution:
            dis = distance(individual.x, solution[medianId].x,
                           individual.y, solution[medianId].y)
            if dis < minNodes['value'] and solution[medianId].cap >= individual.demand:
                minNodes['value'] = dis
                minNodes[individual.id] = medianId
        # found new edge, substract its demand from median capacity

        medianId = minNodes[individual.id]
        median = solution[medianId]
        median.cap -= individual.demand
        # calculate the distance to the median
        distances[medianId] += distance(solution[medianId].x,
                                        individual.x, solution[medianId].y, individual.y)
    return distances


def fitness(solution, genes):
    distances = neighborhoodDistance(solution, genes)
    fit = 0
    for medianId in distances:
        fit += distances[medianId]
        return fit

def inicialFitness(population):
    for solution,genes in population:
        fit = fitness(solution,genes)
        newSolution = Individual(solution,fit)
    #return heap 

def tournament(population):
    number = int(n/10)

    for i in number:
        indiviual = random.uniform(0, n)


with open('input.txt') as file:
    lines = file.readlines()


baseGenes, vertices, medians = inputParse(lines)
population = generateRandomPopulation(n, baseGenes, vertices, medians)
populationHeap = fitness(population)
