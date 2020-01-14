import random


class Vertice(object):
    def __init__(self, x, y, cap, demand):
        self.x = x
        self.y = y
        self.cap = cap - demand
        self.demand = demand
        self.id = random.random()

    def distance(self, x, y): return ((self.x-x)**2 + (self.y-y)**2)**0.5
