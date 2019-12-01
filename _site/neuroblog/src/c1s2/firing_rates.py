import numpy as np

from utils.generate_spikes import random_spikes


# Time length of trial in ms
trial_length = 50

# Spike Count Rate -- number of spikes over duration of the entire trial
num_spikes = np.sum(random_spikes(trial_length))
spike_count_rate = float(num_spikes)/trial_length
print "Spike count rate: {} spikes/ms".format(spike_count_rate)

# Firing Rate -- average number of spikes over a specific short time interval
interval_start = 10
interval_end = 20
num_trials = 100
results = np.zeros(0)
for t in range(0, num_trials):
    num_spikes = np.sum(random_spikes(trial_length)[interval_start - 1: interval_end])
    results = np.append(results, num_spikes)

average_response = np.average(results)
firing_rate = average_response/(interval_end - interval_start)
print "Firing Rate: {} spikes/ms".format(firing_rate)

# Average Firing Rate -- average number of spikes over the entirety of the trial
num_trials = 100
results = np.zeros(0)
for t in range(0, num_trials):
    num_spikes = np.sum(random_spikes(trial_length))
    results = np.append(results, num_spikes)

average_response = np.average(results)
average_firing_rate = average_response/trial_length
print "Average Firing Rate: {} spikes/ms".format(average_firing_rate)
