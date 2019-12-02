import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from utils.generate_spikes import random_spikes


# Length of trial in ms
trial_length = 3000
spikes = random_spikes(trial_length)
fill = np.zeros(500)
spikes = np.concatenate((fill, spikes, fill))

# Create a boxcar (square/rectangular) window and apply it to spike output
b = signal.boxcar(100)
boxcar_spikes = np.convolve(b, spikes)

# Create a Gaussian (curvy) window and apply it to spike count
g = signal.gaussian(500, std=100)
gaussian_spikes = np.convolve(g, spikes)
fill = np.zeros(250)
gaussian_spikes = np.concatenate((gaussian_spikes[250:4000], fill))

# Plot the spikes and the smoothed spikes
fig = plt.figure()

# Spikes
plt.subplot(311)
plt.plot(spikes, 'r', linewidth=0.2)
plt.xlim(0, 4000)
plt.ylabel('Spikes')

# Boxcar
plt.subplot(312)
plt.plot(boxcar_spikes, 'b', label='Boxcar Window')
plt.xlim(0, 4000)
plt.ylabel('Rate [hz]')

# Gaussian
plt.subplot(313)
plt.plot(gaussian_spikes, 'g', label='Gaussian Window')
plt.xlim(0, 4000)
plt.ylabel('Rate [hz]')
plt.xlabel('Time [ms]')

fig.legend()
plt.show()
