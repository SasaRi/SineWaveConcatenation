from time import time
import numpy as np
import math
import matplotlib.pyplot as plt

nr_samples = 2048 # sampling frequency
test_duration = 4 * nr_samples # in number of samples
start_frequency = 1
output = []

def frequency_generator(k = 1, start_frequency = 1, index = 0):
    
    frequency = k / 2 * index + start_frequency

    return frequency

def initialize_LUT(Amplitude = 1, freq = 1, initial_phase_shift = 0):
    sinewave = []
    for i in range(nr_samples):
        value = Amplitude * math.sin(2 * math.pi * freq * i / nr_samples + initial_phase_shift)
        sinewave.append(value)

    return sinewave


LUT = initialize_LUT()
phase_base = 2 * math.pi * 1 / nr_samples
phase_acc = 0
phase_increment = 2 * math.pi * 1 / (nr_samples / start_frequency)



for i in range(test_duration):
    
    if i == nr_samples:
        end_frequency = 10
        duration_of_chirp = test_duration - nr_samples
        constant = (end_frequency - start_frequency) / duration_of_chirp
        iteration = 0
        current_frequency = frequency_generator(k = constant, start_frequency = start_frequency, index = iteration)
        phase_increment = 2 * math.pi * 1 / (nr_samples / current_frequency)
    elif i > nr_samples:
        iteration += 1
        current_frequency = frequency_generator(k = constant, start_frequency = start_frequency, index = iteration)
        phase_increment = 2 * math.pi * 1 / (nr_samples / current_frequency)

    index = int(phase_acc / phase_base)
    output.append(LUT[index])
    phase_acc += phase_increment
    phase_acc = math.fmod(phase_acc, 2 * math.pi)

plt.plot(output)
plt.grid()
plt.show()

# calculate 1st derivative
output_diff = np.diff(output)
plt.plot(output_diff)
plt.grid()
plt.show()