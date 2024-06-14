from matplotlib import pyplot as plt
fig = plt.figure(figsize=[10,10])
ax = fig.gca()
plt.ion()
plt.axis('equal')
width = 100
height = 100
eventQueue = [[(0.1,1,0.1)]*4997 + [(1,0,1),(1,0,1)] + [(0.1,1,0.1)]*5001,
              [(0.1,1,0.1)]*4991 + [(1,0,1),(1,0,1)] + [(0.1,1,0.1)]*5001,
              [(0.1,1,0.1)]*4997 + [(1,0,1),(1,0,1)] + [(0.1,1,0.1)]*5001,
              [(0.1,1,0.1)]*4800 + [(1,0,1),(1,0,1)] + [(0.1,1,0.1)]*5001,
              [(0.1,1,0.1)]*4911 + [(1,0,1),(1,0,1)] + [(0.1,1,0.1)]*5001,
              [(0.1,1,0.1)]*4997 + [(1,0,.5),(1,0,1)] + [(0.1,1,0.1)]*5001]
boardx = [range(width) for i in range(height)]
boardy = [[i]*width for i in range(height)]
for i in eventQueue*5:
    ax.cla()
    ax.scatter(boardx,boardy, marker = "s", s = 20, c = i)
    plt.pause(0.1)
plt.close()