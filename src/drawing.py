import matplotlib.pyplot as plt
from typing import Iterable
from structure import Point, Face, Edge


def draw_figure(L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    for i in range(len(L)):
        plt.plot([L[i-1][0],L[i][0]],[L[i-1][1],L[i][1]],color = "blue")
        plt.plot(L[i][0], L[i][1], '.',color = 'red')

def draw_traingulation(faces: Iterable[Face]):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()

    for f in faces:         
        for e in f.edges:
            plt.plot([e.origin.x,e.twin.origin.x], [e.origin.y,e.twin.origin.y], color = "blue")
            plt.plot(e.origin.x,e.origin.y,'.',color = 'red',markersize = 10)
    return ax
    
def draw_edges(edges: Iterable[Edge]):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax = plt.gca()
    ax.set_xlim((-1, 7))
    ax.set_ylim((-0.5, 2.5))
    for e in edges:
        plt.plot([e.origin.x,e.twin.origin.x],[e.origin.y,e.twin.origin.y],color = "blue")
        
    plt.show()