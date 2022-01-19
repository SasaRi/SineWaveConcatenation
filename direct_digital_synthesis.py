import math
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger()

freq_base = 1 
Amp_base = 1
nr_samples = 2048

def initialize_LUT(Amplitude = 1, freq = 1, initial_phase_shift = 0):
    sinewave = []
    for k in range(nr_samples):
        value = Amplitude * math.sin(2 * math.pi * freq * k / nr_samples + initial_phase_shift)
        sinewave.append(value)
        # logger.warning("sinewave: %.2f\n", value)

    return sinewave

# create base LUT table based on F = 1 Hz and Fs = 512 Hz
LUT = initialize_LUT(Amplitude=Amp_base, freq=freq_base)

# calculate phase shift increment
frequency = 2
phase_increment = 2 * math.pi / (nr_samples / frequency)

phase_base = 2 * math.pi / nr_samples
phase_acc = 0
output = []
for i in range(2 * nr_samples):
    if i == nr_samples:
        phase_acc = 0
        frequency += 10
        phase_increment = 2 * math.pi / (nr_samples / frequency)
    
    index = int(phase_acc / phase_base)
    output.append(LUT[index])
    phase_acc += phase_increment
    phase_acc = math.fmod(phase_acc, 2 * math.pi)

plt.plot(output)
plt.show()
plt.grid()