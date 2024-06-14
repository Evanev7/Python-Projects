import numpy as np
from matplotlib import pyplot as plt
from numba import jit
from time import time


def mbrot(c, detail, j=None):
    if j == None:
        j = c
    z = c
    for i in range(detail):
        z = z**2 + j
        if abs(z) > 2 and i >= 2:
            return i
    else:
        return True

def plotbrot(detail, itr, area = [[-2,-1.25],[1,1.25]], red = 0.5, j = None):
    x,xx,y,xy=[],[],[],[]
    dst = [area[1][a]-area[0][a] for a in [0,1]]
    for i in range(itr):
                xx.append([])
                xy.append([])
    for i in range(detail):
        for k in range(detail):
            point = complex(area[0][0]+dst[0]*i/detail,area[0][1]+dst[1]*k/detail)
            v = mbrot(point, itr)
            if v == True:
                x.append(point.real)
                y.append(point.imag)
            elif type(v) == int:
                xx[v].append(point.real)
                xy[v].append(point.imag)
    fig = plt.figure(figsize=[15,15*dst[1]/dst[0]])
    ax = fig.gca()
    for i in range(len(xx)):
        try:
            ax.scatter(xx[i],xy[i],color=(0,1-(i/len(xx))**red,1-(i/len(xx))**red))
        except:
            pass
    ax.plot([i[0] for i in area], [i[1] for i in area], ',', color = (1,1,1))
    #ax.plot([-0.1676, -0.1676, -0.1672, -0.1672, -0.1676],[-1.041, -1.0414, -1.0414, -1.041, -1.041], ',')
    #ax.plot([-0.2, -0.2, -0.1, -0.1, -0.2],[-1.1, -1, -1, -1.1, -1.1])
    plt.show()
    
plotbrot(1000, 200, [[-2,-1.25],[1,1.25]], 0.5)