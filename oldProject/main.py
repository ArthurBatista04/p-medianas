from genericAlgorithmFunctions import generateRandomSample, evaluate, selection, crossingOver
from vertice import Vertice
from copy import deepcopy
import random
import math


def inputParse(input):
    lines = []
    vertices, medians = input.pop(0).split()
    total = 0
    for eachLine in input:
        x, y, cap, demand = eachLine.split()
        total += int(demand)
        vertice = Vertice(int(x), int(y), int(cap), int(demand))
        lines.append(vertice)

    return [lines, int(vertices), int(medians), total]


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


baseGenes, vertices, medians, total = inputParse(lines)
population = generateRandomSample(deepcopy(baseGenes), vertices, medians)
evaluate(population)
x = getMin(population)
while(True):
    x = getMin(population)
    father, mother = selection(population)
    child = crossingOver(father, mother, deepcopy(baseGenes), medians)
    highestScore = getMax(population)
    if population[highestScore].fitness > child.fitness:
        population.pop(highestScore)
        population.append(child)
    print(x[0])
# soma = 0
# for i in x[1].medians:
#     print(x[1].medians[i].cap)
#     soma += x[1].medians[i].cap
# for i in x[1].genes:
#     soma += i.cap
# print(soma)
# print(total)
# print(len(population))
# print(len(x[1].medians))
# print(len(x[1].genes))
# print('medianas')
# for i in x[1].medians:
#     print('(' + str(x[1].medians[i].cap)+',' +
#           str(x[1].medians[i].capReal) + ','+str(x[1].medians[i].demand)+')')
# print('other points')
# for i in x[1].genes:
#     print('(' + str(i.x)+','+str(i.y)+')')
