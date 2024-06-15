from random import choice as choose
from matplotlib import pyplot as plt

def saesGame(detail):
    xPts, yPts = [], []
    ol = 3**.5/18
    points = {"A":(-ol,5/6),
              "B":(ol,5/6),
              "C":(-2*ol,4/6),
              "D":(2*ol,4/6),
              "E":(-3*ol,3/6),
              "F":(3*ol,3/6),
              "G":(-4*ol,2/6),
              "H":(4*ol,2/6),
              "X":(0,1),
              "Y":(0,0)}
    opt = ["A","B","C","D","E","F","G","H","X","Y"]
    lasm = "Y"
    x = 0
    y = 0
    for i in range(detail):
        xPts.append(x)
        yPts.append(y)
        if lasm == "Y":
            cropt = ["X"]
        elif lasm == "X":
            cropt = opt[:]
        else:
            x = x
            y = y/2
            lasm = "X"
            continue
        move = choose(cropt)
        x = (x+points[move][0])/2
        y = (y+points[move][1])/2
        lasm = move
    return xPts, yPts, points

p1, p2, p3 = saesGame(10000000)

fig = plt.figure(figsize=[15,15])
ax = fig.gca()
ax.plot(p1, p2, 'g,')
ax.plot(*zip(*list(p3.values())),'ro') #Plots the "Baubles"