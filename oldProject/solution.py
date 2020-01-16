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
            while(len(solution) != numMedians):
                count += 1
                rand = random.randrange(0, numVertices-count)
                candidate = genes.pop(rand)
                if candidate.id not in solution:
                    solution[candidate.id] = candidate

            self.medians = solution
            self.genes = genes
            assert(len(self.medians) == numMedians)
            assert(len(self.genes) == numVertices - numMedians)
            for i in self.medians:
                for j in self.genes:
                    if i == j.id:
                        exit('se fud')
                    # if (self.medians[i].x == j.x) and (self.medians[i].y == j.y):
                    #     print('Id da mediana:'+str(i) + ' Cordenada: ' +
                    #           str(self.medians[i].x)+',' + str(self.medians[i].y) + ')')
                    #     print()
                    #     print('Id do outro no:'+str(i) + ' Cordenada: ' +
                    #           str(j.x)+',' + str(j.y) + ')')

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
        pars = {median: [] for median in self.medians}
        for i in self.medians:
            if self.medians[i].cap != self.medians[i].capReal:
                exit('haha')
        for i in self.genes:
            if i.cap != i.capReal:
                exit('haha')
        soma = 0
        for gene in self.genes:
            minNodes = {}
            min = inf
            for medianId in self.medians:
                dis = gene.distance(
                    self.medians[medianId].x, self.medians[medianId].y)
                if (dis < min) and (self.medians[medianId].cap >= gene.demand):
                    min = dis
                    minNodes[gene.id] = medianId
            # found new edge, substract its demand from median capacity
            if len(minNodes) == 0:
                exit('deu ruim')
                print(gene.demand)
                print()
                for i in self.medians:
                    print(self.medians[i].cap)
            medianId = minNodes[gene.id]
            pars[medianId].append(gene.id)
            median = self.medians[medianId]
            median.cap = median.cap - gene.demand
            # calculate the distance to the median
            distances[medianId] += min
        vector = []
        for i in pars:
            for j in pars[i]:
                if j in vector:
                    exit('erro')
                vector.append(j)
        # print(len(vector))
        return distances

    def fitness(self):
        # calcuates the solutions fitness using the distances of each median to other vertices
        distances = self.findDistances()
        fit = 0
        for medianId in distances:
            fit += distances[medianId]
        self.fitness = fit
