from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from time import time
import numpy as np
from numba import jit
from pyquaternion import Quaternion

class q:
    @jit
    def zero():
        return [0,0,0,0]
    
    @jit
    def basis(n):
        q1 = q.zero()
        q1[n] = 1
        return q1
    
    @jit
    def q(r,a,b,c):
        return [r,a,b,c]
    
    @jit
    def add(q1,q2):
        q3=q.zero()
        for i in range(4):
            q3[i] = q1[i]+q2[i]
        return q3
    
    @jit
    def mult(q1,q2):
        if type(q2) == int:
            q2 = [q2,0,0,0]
        return [q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3],
              q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2],
              q1[0]*q2[2] - q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1],
              q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0]]

    @jit
    def mod(q1):
        return (q1[0]**2 + q1[1]**2 + q1[2]**2 + q1[3]**2)

    @jit
    def print(q1, deg = 3):
        strs = [" + ", "i + ", "j + ", "k"]
        o=''
        for i in range (4):
            if str(q1[i])[::-1].find('.') > 5:
                o+=(str(q1[i]-(q1[i]%(10**-deg)))+strs[i])
            else:
                o+=(str(q1[i])+strs[i])
        print(o)
    
    @jit
    def square(q1):
        return q.mult(q1, q1)
    
def brot(c, detail, j=None):
    if j == None:
        j = c
    z = c
    for i in range(detail): 
        z = z**2 + j
        if q.mod(z) > 2 and i >= 2:
            break
    else:
        return True
    return False
    
def plotbrot(detail, itr, area = [[-2,-2,-2,-2],[2,2,2,2]], ju=None):
    x,y,z,w = [],[],[],[]
    xap, yap, zap, wap = x.append, y.append, z.append, w.append
    dst = [(area[1][a]-area[0][a])/detail for a in range(4)]
    print("Calculating..")
    t = time()
    for i in range(detail):
        #for j in range(1):
            for k in range(detail):
                #for l in range(1):
                    j, l = detail/2, detail/2
                    point = Quaternion([area[0][0]+dst[0]*i,
                             area[0][1]+dst[1]*j,
                             area[0][2]+dst[2]*k,
                             area[0][3]+dst[3]*l])
                    if brot(point, itr, ju):
                        xap(point[0])
                        yap(point[1])
                        zap(point[2])
                        wap(point[3])
            if i == 0:
                t2 = (time()-t)*detail
                print("Estimated calculation time:",t2//0.01*0.01, "seconds")
            #print((time()-t)//0.01*0.01,"seconds passed")
            #print(str(100/detail*i)+"% complete,",(time()-t)/(1/(detail*i+0.0000001)),"seconds remaining")
    t1 = time()-t
    print("Finished Calculating in", t1//0.01*0.01, "seconds")
    print("Estimation Error:", abs(t2-t1)//0.01*0.01)
    fig = plt.figure(figsize=[15,15*dst[1]/dst[0]])
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,z,y, 'o')
    plt.show()

plotbrot(1000,100)