import matplotlib.pyplot as plt
import numpy as np
from scipy import signal, special


# Generate fake data following a Gaussian distribution
num_degrees = 80
r_max = 50
flat_data = np.random.randint(-3, 3, size=num_degrees)
g = r_max * signal.gaussian(num_degrees, 10)

# Transform our data to fit the values of the stimulus attribute
gaussian_data = g + flat_data

# When plotting fake data, let's just plot a few values to simulate the fact
# that we wouldn't have samples for every possible orientaion angle.
orientation = np.arange(-num_degrees / 2, num_degrees / 2)  # Orientation angle in degrees
x = np.arange(-num_degrees / 2, num_degrees / 2, 4)

# Plot a Gaussian tuning curve
plt.plot(x, gaussian_data[0::4], 'ro')
plt.plot(orientation, g)
plt.title('Gaussian Tuning Curve')
plt.xlabel('s (Orientation Angle in Degrees)')
plt.ylabel('Neuron Firing Rate (hz)')
plt.show()

# Now time for the Sigmoidal tuning curve
# Values from the book
s_1_2 = 0.036
r_max = 36.03
grad_s = 0.029
disparity = np.arange(-1.0, 1.0, 0.02)  # Retinal disparity in degrees

# x term in the sigmoidal equation in the book
x = -1 * (s_1_2 - disparity) / grad_s
s = r_max * special.expit(x)

# Generate fake data; First bit shouldn't be negative relative
# to the curve (you can't go below 0 hz), but second bit can fall on either
# side of the curve, which will be in the 35-38 hz range.
flat_data_1 = np.random.randint(0, 3, size=40)
flat_data_2 = np.random.randint(-1, 2, size=60)
flat_data = np.concatenate((flat_data_1, flat_data_2))

# Transform our flat data into sigmoidal data
sigmoidal_data = flat_data + s

## Plot the curve
#plt.plot(disparity, s)
#
## Plot fake data, but simulate not getting a result for every value of s
#x = np.arange(-1.0, 1.0, 0.08)
#plt.plot(x, sigmoidal_data[0::4], 'ro')
#
#plt.title('Sigmoidal Tuning Curve')
#plt.xlabel('s (Retinal Disparity in Degrees)')
#plt.ylabel('Neuron Firing Rate (hz)')
#plt.show()
