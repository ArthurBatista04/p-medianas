import random
import math


class Solution(object):
    def __init__(self):
        self.medians = []
        self.fitness = 0
        self.restOfVertices = []
        self.distances = []

    def randomize(self, vertices, numMedians):
        medianSet = []
        while len(medianSet) != numMedians:
            choicePostion = random.randrange(0, len(vertices))
            newMedian = vertices.pop(choicePostion)
            medianSet.append(newMedian)
        self.medians = medianSet
        self.restOfVertices = vertices

    def initChild(self, medians, allVertices):
        for median in medians:
            for pos, vertice in enumerate(allVertices):
                if vertice.id == median.id:
                    allVertices.pop(pos)
        self.medians = medians
        self.restOfVertices = allVertices
        self.calculateFitness()

    def defineMinimalDistance(self):
        restOfVertices = self.restOfVertices
        medians = self.medians
        distances = {median.id: [] for median in medians}
        for pos, rest in enumerate(restOfVertices):
            min = math.inf
            newMedianId = None
            for median in medians:
                if (rest.distance(median.x, median.y) < min) and (rest.demand <= median.cap):
                    min = rest.distance(median.x, median.y)
                    newMedianId = median.id
            distances[newMedianId].append(rest)
            median = self.getMedianById(newMedianId)
            median.cap -= rest.demand
        self.distances = distances

    def getMedianById(self, id):
        for median in (self.medians):
            if median.id == id:
                return median

    def calculateFitness(self):
        self.defineMinimalDistance()
        medians = self.distances
        for medianId in medians:
            for rest in medians[medianId]:
                median = self.getMedianById(medianId)
                xMedian = median.x
                yMedian = median.y
                self.fitness += rest.distance(
                    xMedian, yMedian)
        # if self.fitness < 660:
        #     print(self.fitness)
        #     leng = 0
        #     for pos, i in enumerate(medians):
        #         median = self.getMedianById(i)
        #         print('mediana: ' + str(pos))
        #         print('Posicao x y: ', end=" ")
        #         print('(', median.x, ',', median.y, ')')
        #         print('Ligacoes')
        #         for j in medians[i]:
        #             print('Posicao x y: ', end=" ")
        #             print('(', j.x, ',', j.y, ')')
        #         print()
        #     exit()
        for vertice in self.medians:
            vertice.cap = vertice.capReal
        for vertice in self.restOfVertices:
            vertice.cap = vertice.capReal
