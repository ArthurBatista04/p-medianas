from copy import copy
from random import


class Vertice(object):
    def __init__(self, x, y, cap, demand):
        self.x = x
        self.y = y
        self.cap = cap - demand
        self.demand = demand


def inputParse(input):
    lines = []
    vertices, medians = input.pop(0).split()
    for eachLine in input:
        x, y, cap, demand = eachLine.split()
        vertice = Vertice(int(x), int(y), int(cap), int(demand))
        lines.append(vertice)
    return [lines, vertices, medians]


def inicialSol(inicialSet):
    inicialSol = []
    numbers = random.randint(0, vertices)
    for i in medians:
        inicialSol.append(inicialSet.pop(numbers[i]))


def calculateEdges(newMedians, inicialSet):
    # calcular as distancias para cada vertice com cada mediana e escolher a menor


with open('input.txt') as file:
    lines = file.readlines()

cromos, vertices, medians = inputParse(lines)
inicialSet = cromos.copy()
newMedians = inicialSol(inicialSet)
