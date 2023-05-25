import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 11), ylim=(0, 10))

# https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html
# args -- center, r, theta1, theta2
patch = mpatches.Wedge((1,9), 1, 26, 0, fc='dodgerblue', ec="none")


def init():
    patch.center = (1,9)
    patch.theta2 = 270
    ax.add_patch(patch)
    return patch,


def animate(frame):
    x,y = patch.center
    t2 = 345+40*np.cos(frame*np.radians(15))

    if (frame <= 25):
        x = frame / 2.5
        x = 1 if x < 1 else x
        y = 9
    elif (frame > 25 and frame <= 50):
        x = 10
        y = 9 - (frame - 26) * 0.32
    elif (frame > 50 and frame <= 75):
        x = 10 - (frame - 51) * 0.36
        y = 1
    else:
        x = 1
        y = 1 + (frame - 76) * 0.33

    patch.center = (x, y)
    patch.theta2 = t2

    patch._recompute_path()
    return patch,


# frames - the number of frames for the animation,
# interval - the delay between frames in milliseconds
# Setting blit=True makes the animation more efficient
# by only redrawing the parts of the plot that have changed in each frame.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
anim.save('./animation.gif', writer='imagemagick', fps=30)

plt.show()
