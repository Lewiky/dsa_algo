class ListGraph:

    def __init__(self,v,e):
        self.v = v
        self.e = e

class MatrixGraph:

    def __init__(self,A):
        self.matrix = A

class Node:

    def __init__(self, val):
        self.val = val

class Edge:

    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight
