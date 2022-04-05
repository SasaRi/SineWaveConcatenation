"""
This test will simulate the change of frequency by using DDS method. First sine wave is generated with fixed frequency. 
At the half of the test, frequency is changed instantly. 
Base block of this test is a LUT. Amplitude is fixed the whole time. 
"""

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
frequency_1 = 10
phase_increment = 2 * math.pi / (nr_samples / frequency_1)

phase_base = 2 * math.pi / nr_samples
phase_acc = 0
output = []
is_frequency_changed = 0

for i in range(range_for_loop):
    if i > range_for_loop / 2 and is_frequency_changed == 0:
        if output[-1] - output[-2] < 0.0004:
            frequency_2 = frequency_1 + 10
            is_frequency_changed = 1
            phase_increment = 2 * math.pi / (nr_samples / frequency_2)
            logger.warning("phase value before generating the new chunk: %.2f [deg]\n", phase_acc * 180 / math.pi)
    
    index = round(phase_acc / phase_base)
    # logger.warning("index: %.d\n", index)
    if index == nr_samples:
        index = 0
    output.append(LUT[index])
    phase_acc += phase_increment
    phase_acc = math.fmod(phase_acc, 2 * math.pi)

plt.plot(output)
plt.title("Sine wave with instant change of frequency from " + str(frequency_1) + " Hz to " + str(frequency_2) + " Hz")
plt.xlabel("Number of samples")
plt.grid()
plt.show()

# calculate 1st derivative
output_diff = np.gradient(output)
plt.title("1st derivative of the Sine wave with instant change of frequency from " + str(frequency_1) + " Hz to " + str(frequency_2) + " Hz")
plt.xlabel("Number of samples")
plt.plot(output_diff)
plt.grid()
plt.show()