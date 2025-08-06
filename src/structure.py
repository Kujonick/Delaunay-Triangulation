from __future__ import annotations
from typing import Optional

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.edges = set()
    
    def __hash__(self):
        return hash(self.x)*3 + hash(self.y)*5
    
    def __eq__(self,other):
        if not isinstance(other,Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return "P:("+str(self.x)+","+str(self.y)+")"
    

class Edge:

    def __init__(self,origin: Point):
        self.origin: Point = origin
        self.next: Edge= None
        self.prev: Edge= None
        self.face: Face= None
        self.twin: Edge= None

    @classmethod
    def create_edge(cls, point1: Point, point2: Point):
        e1 = Edge(point1)
        e2 = Edge(point2)
        e1.twin=e2
        e2.twin=e1
        point1.edges.add(e1)
        point2.edges.add(e2)
        return e1
        
    def __hash__(self):
        return hash(self.origin)*7 + hash(self.twin.origin)
    
    def __eq__(self, other):
        if not isinstance(other,Edge):
            return False
        return self.origin == other.origin and self.twin.origin == other.twin.origin
    
    def __str__(self):
        return "E: "+ str(self.origin) + " -> " + str(self.twin.origin)
    
    def orient(self:Edge, p: Point) -> float:
        A = self.origin
        B = self.twin.origin
        wynik = A.x*B.y + B.x*p.y + p.x*A.y - A.y*B.x - B.y*p.x - A.x*p.y
        if abs(wynik)<10**(-12):
            return 0
        return wynik
    
    @staticmethod
    def connect_two(first: Edge, second: Edge):
        second.prev = first
        first.next = second


class Face:
    def __init__(self, e1:Edge, e2:Edge, e3:Edge):
        self.edges = set([e1,e2,e3])
        self.visited = False
    
    def __hash__(self):
        result = 1
        for e in self.edges:
            result*=hash(e)
        return result
    
    def __eq__(self,other):
        if not isinstance(other,Face):
            return False
        if len(self.edges) != len(other.edges):
            return False
        for e in self.edges:
            if e not in other.edges:
              return False
        return True
    
    def __str__(self):
        string = "__"
        for e in self.edges:
            string = string + str(e) + " _|_ "
        return "F: " + string
    
    def point_inside_circle(self, p):
        '''function that checks, if the point is inside the circle writen over the triangle'''
        first = list(self.edges)[0]
        edges = [first, first.next, first.prev]
        
        points = [edges[i].origin for i in range(3)]
        result = 0
        for i in range(3):
            result += (points[i].x - p.x)*(points[(i+1)%3].y - p.y)*(points[(i+2)%3].x**2 - p.x**2 + points[(i+2)%3].y**2 - p.y**2)
            result -= (points[i].x - p.x)*(points[(i+2)%3].y - p.y)*(points[(i+1)%3].x**2 - p.x**2 + points[(i+1)%3].y**2 - p.y**2)
        if abs(result)<10**(-12):
            return 0
        return result