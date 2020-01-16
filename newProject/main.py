from vertice import Vertice
from geneticAlgorithm import generateRandomPopulation, populationFitness, selection, crossingOver
import copy
import math


def inputParse():
    with open('input.txt') as file:
        lines = file.readlines()
    allVertices = []
    vertices, medians = lines.pop(0).split()
    for eachLine in lines:
        x, y, cap, demand = eachLine.split()
        vertice = Vertice(float(x), float(y), float(cap), float(demand))
        allVertices.append(vertice)

    return [allVertices, int(vertices), int(medians)]


def getWeakestFitness(population):
    weakest = math.inf
    for solution in (population):
        if solution.fitness < weakest:
            weakest = solution.fitness
    return weakest


def getStrongestFitness(population):
    strongest = -math.inf
    strongestIndice = 0
    for indice, solution in enumerate(population):
        if solution.fitness > strongest:
            strongest = solution.fitness
            strongestIndice = indice
    return strongestIndice, strongest


vertices, numVertices, numMedians = inputParse()
population = generateRandomPopulation(
    copy.deepcopy(vertices), numVertices, numMedians)
populationFitness(population)
fit = getWeakestFitness(population)
while(True):
    father, mother = selection(population)
    child = crossingOver(father, mother, copy.deepcopy(vertices))
    indice, strongestFit = getStrongestFitness(population)
    if child.fitness < strongestFit:
        population.pop(indice)
        population.append(child)
    fit = getWeakestFitness(population)
    print(fit)
