from genericAlgorithmFunctions import generateRandomSample, evaluate, selection, crossingOver
from vertice import Vertice
from copy import deepcopy
import random
import math


def inputParse(input):
    lines = []
    vertices, medians = input.pop(0).split()
    for eachLine in input:
        x, y, cap, demand = eachLine.split()
        vertice = Vertice(int(x), int(y), int(cap), int(demand))
        lines.append(vertice)
    return [lines, vertices, medians]


def getMin(population):
    min = math.inf
    for i in population:
        if min > i.fitness:
            min = i.fitness
            filho = i
    return min, i


def getMax(population):
    max = -math.inf
    for pos, i in enumerate(population):
        if max < i.fitness:
            max = i.fitness
            pol = pos
    return pol


with open('input.txt') as file:
    lines = file.readlines()


baseGenes, vertices, medians = inputParse(lines)
population = generateRandomSample(baseGenes, vertices, medians)
evaluate(population)
x = getMin(population)
while(x[0] > 970):
    x = getMin(population)
    father, mother = selection(population)
    child = crossingOver(father, mother, deepcopy(baseGenes))
    randPos = getMax(population)
    if population[randPos].fitness > child.fitness:
        population.pop(randPos)
        population.append(child)
    print(x[0])
# for i in x[1].medians:
#     print(i.x)
#     print
# print(x[1].medians)
