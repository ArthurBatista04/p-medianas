from solution import Solution
from copy import deepcopy
import random
import uuid
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


def crossingOver(father, mother, genes):
    childGenes = {}
    for fatherMedianId in father.medians:
        for motherMedianId in mother.medians:
            if fatherMedianId == motherMedianId:
                childGenes[fatherMedianId] = father.medians[fatherMedianId]
                father.medians[fatherMedianId].cap = father.medians[fatherMedianId].capReal
    while len(childGenes) != 12:
        indice = random.choice(list(mother.medians))
        if indice not in childGenes:
            childGenes[indice] = mother.medians[indice]
            mother.medians[indice].cap = mother.medians[indice].capReal
        indice = random.choice(list(father.medians))
        if (len(childGenes) != 12) and (indice not in childGenes):
            childGenes[indice] = father.medians[indice]
            father.medians[indice].cap = father.medians[indice].capReal
    child = Solution()
    child.initChild(childGenes, genes)
    return child
