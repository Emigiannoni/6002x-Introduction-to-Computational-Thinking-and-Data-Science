# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:07:43 2022

@author: Emi
"""

''' DEEP FIRST SEARCH '''


def printPath(path):
    '''Assumes path is a list of nodes'''
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path)-1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    '''Assumes graph is a Digraph, start and end are nodes, path and shortest
    are list of nodes. Returns a shortest path from start to end in graph'''
    path = path + [start]
    if toPrint:
        print('Current DFS path: ', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            newPath = DFS(graph, node, end, path, shortest, toPrint)
            if newPath != None:
                shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest


def DFSshortestPath(graph, start, end, toPrint=False):
    '''Assumes graph is a Digraph, start and end are nodes.
       Returns a shortest path from start to end in graph'''
    return DFS(graph, start, end, [], None, toPrint)


''' BREADHT FIRST SEARCH '''


def BFS(graph, start, end, toPrint=False):
    '''Assumes graph is a Digraph, start and end are nodes.
    Returns a shortest path from start to end in graph'''
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path: ', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None
    

def BFSshortestPath(graph, start, end, toPrint=False):
    '''Assumes graph is a Digraph, start and end are nodes.
       Returns a shortest path from start to end in graph'''
    return BFS(graph, start, end, toPrint)
