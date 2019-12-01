import numpy as np
from scipy import signal


def random_spikes(size):
    """
    Generate several random spikes in an array of size=size
    """
    spikes = np.random.random_integers(0, 1, size)
    for i, s in enumerate(spikes):
        if i < len(spikes) - 1 and (spikes[i] == 1 and spikes[i + 1] == 1):
            spikes[i] = 0
    return spikes
