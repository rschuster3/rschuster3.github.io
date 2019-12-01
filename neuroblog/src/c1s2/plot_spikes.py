import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from utils.generate_spikes import random_spikes


# Pad output with a flat line for aesthetic purposes
flat = np.array([0, 0, 0, 0, 0])

#output = flat
#for s in np.random.random_integers(0, 4, 10):
#    impulse = signal.unit_impulse(5, s)
#    output = np.concatenate((output, impulse))
#output = np.concatenate((output, flat))

# Make several spikes and concatenate them
out = random_spikes(50)
out = np.concatenate((flat, out, flat))

# Plot the spikes
plt.plot(np.arange(0, 60), out)
plt.margins(0.1, 0.1)
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.title('Several Neural Spikes')
plt.grid(True)
plt.show()
