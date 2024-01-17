import matplotlib.pyplot as plt
import numpy as np 

from matplotlib.patches import Ellipse 

NUM = 250

np.random.seed(19680801)
NUM = 250

ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), 
                height=np.random.rand(),
                angle=np.random.rand() *360)
        for i in range(NUM)]

fix, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 10), aspect="equal")

for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

plt.show()