import random
from math import inf


class Solution(object):
    medians = None
    Genes = None
    fitness = 0

    def __init__(self, genes, numVertices, numMedians):
        # Generates a random solution with medianas vertices
        count = 0
        solution = {}
        for i in range(numMedians):
            count += 1
            rand = random.randint(0, numVertices-count)
            candidate = genes.pop(rand)
            solution[candidate.id] = candidate
        self.medians = solution
        self.genes = genes

    def findDistances(self):
        # find the neartes neighbors to the medians and calculate there distance
        distances = {median: 0 for median in self.medians}
        for gene in self.genes:
            minNodes = {'value': inf}
            for medianId in self.medians:
                dis = gene.distance(
                    self.medians[medianId].x, self.medians[medianId].y)
                if dis < minNodes['value'] and self.medians[medianId].cap >= gene.demand:
                    minNodes['value'] = dis
                    minNodes[gene.id] = medianId
            # found new edge, substract its demand from median capacity

            medianId = minNodes[gene.id]
            median = self.medians[medianId]
            median.cap -= gene.demand
            # calculate the distance to the median
            distances[medianId] += gene.distance(self.medians[medianId].x,
                                             self.medians[medianId].y,)
        return distances

    def fitness(self):
        # calcuates the solutions fitness using the distances of each median to other vertices
        distances = self.findDistances()
        fit = 0
        for medianId in distances:
            fit += distances[medianId]
        self.fitness = fit
