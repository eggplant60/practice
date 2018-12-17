import numpy as np
import pylab
import matplotlib.pyplot as plt

def on_pick(event):
    line = event.artist
    xdata, ydata = line.get_data()
    ind = event.ind
    print('on pick line {} [{} {}]'.format(ind, xdata[ind], ydata[ind]))

fig, ax = plt.subplots()
ax.plot(np.random.rand(10), 'o', picker=5)
cid = fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()
