import random
from math import inf
import uuid


class Solution(object):
    medians = None
    genes = None
    fitness = 0

    def __init__(self, genes=None, numVertices=None, numMedians=None):
        # Generates a random solution with medianas vertices
        if genes != None:
            count = 0
            solution = {}
            for i in range(numMedians):
                count += 1
                rand = random.randint(0, numVertices-count)
                candidate = genes.pop(rand)
                solution[candidate.id] = candidate
            self.medians = solution
            self.genes = genes

    def initChild(self, medians, genes):
        self.medians = medians
        newGenes = []
        for gene in genes:
            if gene.id not in self.medians:
                newGenes.append(gene)
        self.genes = newGenes
        self.fitness()

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
