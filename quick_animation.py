import IPython
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from src.data import *

if __name__ == "__main__":
    FEATURES = {
        "depth", "adjacent", "contour", "median", "laplacian", "gradangle"
    }

    all_data = load_all_processed()
    sample = next(iter(all_data.values()))


    def animate(frames: np.ndarray, interval: int = 100):
        fig = plt.figure()
        im = plt.imshow(frames[0], animated=True)

        def update(f):
            im.set_data(frames[f])
            return im,

        return animation.FuncAnimation(
            fig, func=update, blit=True, frames=len(frames), interval=interval
        )


    def animate_sample(idx: str, feature: str = "depth"):
        assert feature in FEATURES
        frames = all_data[idx]
        frames = frames[feature]
        return animate(frames)

    for feature in FEATURES:
        anim = animate_sample("9162_20210202_adj10_floor5000", feature)
        anim.save(f"cow_anim_{feature}.gif")
        plt.clf()
