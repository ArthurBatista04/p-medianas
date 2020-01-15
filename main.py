from genericAlgorithmFunctions import generateRandomSample, evaluate, selection, crossingOver
from vertice import Vertice
from copy import deepcopy


def inputParse(input):
    lines = []
    vertices, medians = input.pop(0).split()
    for eachLine in input:
        x, y, cap, demand = eachLine.split()
        vertice = Vertice(int(x), int(y), int(cap), int(demand))
        lines.append(vertice)
    return [lines, vertices, medians]


with open('input.txt') as file:
    lines = file.readlines()


baseGenes, vertices, medians = inputParse(lines)
population = generateRandomSample(baseGenes, vertices, medians)
evaluate(population)
father, mother = selection(population)
child = crossingOver(father, mother, deepcopy(baseGenes))
print(father.fitness)
print(mother.fitness)
print(child.fitness)
