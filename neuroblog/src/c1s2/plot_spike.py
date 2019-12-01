import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


# Plot a single dirac delta fcn spike
output = signal.unit_impulse(50, 30)

plt.plot(np.arange(0, 50), output)
plt.margins(0.1, 0.1)
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.title('A Single Neural Spike')
plt.grid(True)
plt.show()
