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


def mutation(childGenes, allGenes, medians):
    raffle = random.randrange(0, 2)
    if raffle == 1:
        geneId = random.choice(list(childGenes))
        del childGenes[geneId]
        while (len(childGenes) != medians):
            newPos = random.randrange(0, len(allGenes))
            newGene = allGenes[newPos]
            if newGene.id not in childGenes:
                childGenes[newGene.id] = newGene


def crossingOver(father, mother, genes, medians):
    childGenes = {}
    assert(len(mother.medians) == medians)
    assert(len(father.medians) == medians)
    for fatherMedianId in father.medians:
        for motherMedianId in mother.medians:
            if fatherMedianId == motherMedianId:
                childGenes[fatherMedianId] = deepcopy(
                    father.medians[fatherMedianId])
                childGenes[fatherMedianId].cap = father.medians[fatherMedianId].capReal
    while len(childGenes) != medians:
        indice = random.choice(list(mother.medians))
        if indice not in childGenes:
            childGenes[indice] = deepcopy(mother.medians[indice])
            childGenes[indice].cap = childGenes[indice].capReal
        indice = random.choice(list(father.medians))
        if (len(childGenes) != medians) and (indice not in childGenes):
            childGenes[indice] = deepcopy(father.medians[indice])
            childGenes[indice].cap = childGenes[indice].capReal
    mutation(childGenes, genes, medians)
    child = Solution()
    child.initChild(childGenes, genes)
    return child
