# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:47:20 2022

@author: Emi Giannoni

Node: Objeto que representa cada nodo del grafo.
Edge: Ojeto que representa la relacion entre 2 elementos del grafo.
      Si A esta relacionado con B debe existir un edege [A] = B
WeightedEdge: amplia edge permitiendo asignar un peso a cada relacion.
Digraph: objeto base para construir un grafo unidireccional.
Graph: amplia Digraph permitiendo relaciones ida y vuelta.

"""


class Node(object):

    def __init__(self, name):
        '''Assumes 'name' is a string'''
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):

    '''Edge objects contains the relationship between two nodes'''

    def __init__(self, src, dest):
        '''Assumes 'src' (source) and 'dest' (destination) are nodes'''
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):

    '''Extends Edge object taking into consideration a weight for each edge'''

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + \
            ' (' + str(self.weight) + ')'


class Digraph(object):

    def __init__(self):
        '''Edges is a dictionary containing the relation between nodes'''
        '''Edges keys are the sources nodes, and their values are the posibles
        destinations from these node'''
        self.edges = {}

    def addNode(self, node):
        '''Inserts node into edges dictionary'''
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        '''Source and destination must be included in a Edge objetc before
        adding them into de Graph'''
        src = edge.getSource()
        dest = edge.getDestination()
        '''Both nodes must be included in Edge dictionary'''
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in Graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]  # this las action is executed to omit las new line


class Graph(Digraph):
    '''Graph object was implemented over Digraph object, but rewriting addEdge
    method in order to make the relationship bidirectional'''

    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        '''Rev is a new Edge object containing the inverse relation
        of provided nodes'''
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
