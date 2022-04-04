"""
This generator will be based on a direct digital synthesis method (samples are generated on the fly, method returns the next value in the wave).
Frequency change will happen instantly and amplitude will be a function of time.
"""

import math
import matplotlib.pyplot as plt
import logging
import numpy as np

logger = logging.getLogger()

nr_samples = 2048 # sampling frequency
phase_base = 2 * math.pi / (nr_samples / 1) # 1 is a base frequency of LUT sinewave
phase_acc = 0
sinewave = []
is_frequency_changed = 0
is_amplitude_changed = 0
index_when_amplitude_changed = 0

# direct digital synthesis method is based on a LUT table (basic sine wave for some amplitude and frequency)
# in this case we used y(t) = 1 * sin(2 * pi * 1 * t + 0)
def initialize_LUT(Amplitude = 1, Freq = 1, theta = 0):
    output = []
    for k in range(nr_samples):
        value = Amplitude * math.sin(2 * math.pi * Freq * k / nr_samples + theta)
        output.append(value)

    return output

def amplitude_change(Amp_start = 1, Amp_final = 1, index = 0, transition_time = 1):
    # amplitude change rate
    k = (Amp_final - Amp_start) / transition_time
    
    amplitude = k * index + Amp_start

    return amplitude


# main application
AMPLITUDE_0 = 1
AMPLITUDE_1 = 10
FREQUENCY_0 = 10
FREQUENCY_1 = 20

LUT = initialize_LUT()

frequency = FREQUENCY_0
amplitude = AMPLITUDE_0

loop_range = 4000
for i in range(loop_range):
    # in the middle of the experiment command the change the frequency
    if i > loop_range / 3 and is_frequency_changed == 0:
        # frequency can be changed when 1st derivative is approx. equal to 0
        # the problem is that threshold value can't be hard-coded, it changes with the change of frequencies, 
        # e.g. 0.0004 works well only for a 10 Hz sinewave
        # there has to be a mathematical solution that will search for a 1st derivative minuimum
        if math.fabs(sinewave[-1] - sinewave[-2]) < 0.0005:
            is_frequency_changed = 1
            frequency = FREQUENCY_1
            logger.warning("phase value before generating the new chunk: %.2f [deg]\n", phase_acc * 180 / math.pi)
            logger.warning("index when frequency changed : %d\n", i)

    # calculate initial phase shift increment for given frequency
    phase_increment = 2 * math.pi / (nr_samples / frequency)
    
    index = round(phase_acc / phase_base)
    # logger.warning("index: %.d\n", index)
    if index == nr_samples:
        index = 0

    value = LUT[index]

    # somewhere in the experiment change the amplitude as well
    if i > loop_range / 2 and is_frequency_changed == 1 and is_amplitude_changed == 0:
        is_amplitude_changed = 1
        index_when_amplitude_changed = i
        logger.warning("index when amplitude changed is: %d\n", index_when_amplitude_changed)

    if is_amplitude_changed == 1:
        index_for_amplitude = i - index_when_amplitude_changed        
        amplitude = \
            amplitude_change(Amp_start=AMPLITUDE_0, Amp_final=AMPLITUDE_1, index=index_for_amplitude, transition_time=loop_range - index_when_amplitude_changed)

    sinewave.append(amplitude * value)
    phase_acc += phase_increment
    phase_acc = math.fmod(phase_acc, 2 * math.pi)

plt.plot(sinewave)
plt.title("Sinewave based on dds, frequency is changed instantly while amplitude is a function of time")
plt.xlabel("Number of samples")
plt.grid()
plt.show()

sinewave_diff = np.gradient(sinewave)
plt.plot(sinewave_diff)
plt.title(" 1st derivative Sinewave based on dds, frequency is changed instantly while amplitude is a function of time")
plt.xlabel("Number of samples")
plt.grid()
plt.show()