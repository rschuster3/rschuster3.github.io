import numpy as np
from scipy import signal


def random_spikes(size):
    """
    Generate zeros and ones in an array of size=size.
    probabilities = [probability 0 will appear, probability 1 will appear]
    """
    spikes = np.random.choice(2, size, p=[0.99, 0.01])

    # Get rid of spikes that are on top of each other
    for i, s in enumerate(spikes):
        if i < len(spikes) - 1 and (spikes[i] == 1 and spikes[i + 1] == 1):
            spikes[i] = 0
    return spikes
