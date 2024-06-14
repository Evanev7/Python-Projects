import numpy as np
from numpy.random import choice
from time import time
from matplotlib.pyplot import plot
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numba import jit

def shape(sides, size = 1, rotation = np.pi/2):
    s=[]
    for i in range(sides):
        phi = rotation + i*2*np.pi/sides
        s.append([size * np.cos(phi), size * np.sin(phi)])
    return s

def chaosGame(points, rules, **kwargs):
    dkeys = ["exclude", "detail", "zoom", "moveX", "moveY", "rotation"]
    defaults = {"exclude":[], "detail":1000000,"zoom":1,"moveX":0,"moveY":0, "rotation":np.pi/2}
    for i in range(len(defaults)):
        try:
            kwargs[dkeys[i]]
        except KeyError:
            kwargs[dkeys[i]] = defaults[dkeys[i]]
    if type(points) == int:
        s=[]
        for i in range(points):
            phi = kwargs["rotation"] + i*2*np.pi/points
            s.append([np.cos(phi), np.sin(phi)])
        points = s
    print(kwargs)
    nextPoint = [i for i in choice(len(points), kwargs["detail"])]
    x, y = [], []
    mxx, mxy = max([i[0] for i in points]), max([i[1] for i in points])
    mnx, mny = min([i[0] for i in points]), min([i[1] for i in points])
    lastX, lastY = 0, 0
    lastPoint = nextPoint[0]
    for i in range(kwargs["detail"]):
        if nextPoint[i] in [(rules[i] + lastPoint)%len(points) for i in range(len(rules))]:
            continue
        skip = False
        for j in kwargs["exclude"]:
            if j[0][0] <= (lastX + points[nextPoint[i]][0])/2 <= j[1][0] and j[0][1] <= (lastY + points[nextPoint[i]][1])/2 <= j[1][1]:
                skip = True
        if skip:
            continue
        lastX = (lastX + points[nextPoint[i]][0])/2
        lastY = (lastY + points[nextPoint[i]][1])/2
        if ((mnx+kwargs["moveX"])/kwargs["zoom"] <= lastX <= (mxx+kwargs["moveX"])/kwargs["zoom"]
        and (mny+kwargs["moveY"])/kwargs["zoom"] <= lastY <= (mxy+kwargs["moveY"])/kwargs["zoom"]): 
            x.append(lastX)
            y.append(lastY)
        lastPoint = nextPoint[i]
    for i in range(4):
        x.append([(mxx+kwargs["moveX"])/kwargs["zoom"],
                  (mxx+kwargs["moveX"])/kwargs["zoom"],
                  (mnx+kwargs["moveX"])/kwargs["zoom"],
                  (mnx+kwargs["moveX"])/kwargs["zoom"]][i])
        y.append([(mxx+kwargs["moveY"])/kwargs["zoom"],
                  (mnx+kwargs["moveY"])/kwargs["zoom"],
                  (mxx+kwargs["moveY"])/kwargs["zoom"],
                  (mnx+kwargs["moveY"])/kwargs["zoom"]][i])
    plt.ion()
    for i in range(int((len(x)/10)//1)):
        for j in range(10):
            plt.scatter(x[i*10+j],y[i*10+j], marker='.')  
        plt.pause(0.01)

chaosGame(4, [1 ], rotation=np.pi/4)