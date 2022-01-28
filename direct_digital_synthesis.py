import math
import matplotlib.pyplot as plt
import logging
import numpy as np

logger = logging.getLogger()

freq_base = 1 
Amp_base = 1
nr_samples = 2048
range_for_loop = 5000

def initialize_LUT(Amplitude = 1, freq = 1, initial_phase_shift = 0):
    sinewave = []
    for k in range(nr_samples):
        value = Amplitude * math.sin(2 * math.pi * freq * k / nr_samples + initial_phase_shift)
        sinewave.append(value)
        # logger.warning("sinewave: %.2f\n", value)

    return sinewave

# create base LUT table based on F = 1 Hz, Fs = 2048 Hz and Amp = 1
LUT = initialize_LUT(Amplitude=Amp_base, freq=freq_base)

# calculate phase shift increment
frequency = 1
phase_increment = 2 * math.pi / (nr_samples / frequency)

phase_base = 2 * math.pi / nr_samples
phase_acc = 0
output = []
for i in range(range_for_loop):
    if i == range_for_loop / 2:
        frequency += 30
        phase_increment = 2 * math.pi / (nr_samples / frequency)
    
    index = round(phase_acc / phase_base)
    if index == nr_samples:
        index = 0
    output.append(LUT[index])
    phase_acc += phase_increment
    phase_acc = math.fmod(phase_acc, 2 * math.pi)

plt.plot(output)
plt.grid()
plt.show()

# calculate 1st derivative
output_diff = np.gradient(output)
plt.plot(output_diff)
plt.grid()
plt.show()