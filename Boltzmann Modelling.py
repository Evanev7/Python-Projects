from random import randint
n = 100
level = 2
iterations = 10
levels, count = [0,1,2], [0,0,n]
data = [[levels,count]]
for i in range(iterations):
    r = [randint(0,n-1),randint(0,n-1)]
    for j in [0,1]:
        c=0
        while r[j] > 0:
            r[j] -= count[c]
            c += 1
        if c < 2 and j == 0:
            done = False
            while not done:
                _ = randint(0,n-1)
                q=0
                while _ > 0:
                    _ -= count[q]
                    q += 1                        
                if q >= 2:
                    done = True
            c=q
        count[c-1] -= 1
        while c+int((j+1)/2)>levels[-1]:
            levels.append(levels[-1]+1)
            count.append(0)
        count[c+int((j+1)/2)]+=1
    data.append([levels,count])
print(data)
from matplotlib import pyplot as plt
fig = plt.figure(figsize=[10,10])
ax = fig.gca()
plt.ion()

for i in data:
    ax.cla()
    ax.plot(i[0],i[1])
    plt.pause(1)
plt.close()