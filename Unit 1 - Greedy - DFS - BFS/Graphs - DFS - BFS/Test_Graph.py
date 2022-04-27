# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:35:38 2022

@author: Emi Giannoni
"""
import Graph_Classes as gc
from Search_Algorithms import DFSshortestPath, BFSshortestPath, printPath


def buildCityGraph():
    g = gc.Digraph()

    citys = ['Boston', 'Providence', 'New York', 'Chicago', 'Denver',
             'Phoenix', 'Los Angeles']

    for name in citys:
        g.addNode(gc.Node(name))

    g.addEdge(gc.Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(gc.Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(gc.Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(gc.Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(gc.Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(gc.Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(gc.Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(gc.Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(gc.Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(gc.Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


print(buildCityGraph())


def testSP_DFS(source, destination):

    print('*** Testing DFS ***')    

    g = buildCityGraph()
    sp = DFSshortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print('Shortest path from ', source, ' to ', destination, ' is ', printPath(sp))
    else:
        print('There is no path from ', source, ' to ', destination)


testSP_DFS('Los Angeles', 'Phoenix')


def testSP_BFS(source, destination):
    
    print('*** Testing BFS ***')  

    g = buildCityGraph()
    sp = BFSshortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)
    
    if sp != None:
        print('Shortest path from ', source, ' to ', destination, ' is ', printPath(sp))
    else:
        print('There is no path from ', source, ' to ', destination)


testSP_BFS('Los Angeles', 'Phoenix')