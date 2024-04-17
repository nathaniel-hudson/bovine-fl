import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def animate(frames: np.ndarray, interval: int = 100) -> animation.FuncAnimation:
    fig = plt.figure()
    im = plt.imshow(frames[0], animated=True)

    def update(f):
        im.set_data(frames[f])
        return (im,)

    return animation.FuncAnimation(
        fig, func=update, blit=True, frames=len(frames), interval=interval
    )
