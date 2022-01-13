import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig
import math
import logging

logger = logging.getLogger()

theta = 0
t_start = 0
t_end = 0.08
fs = 13500
nr_samples = int((t_end - t_start) * fs)
time = np.linspace(t_start, t_end, num = nr_samples)

def generate_sinewave(Amp : float = 1, freq : float = 50):

    global theta

    sinewave = Amp * np.sin(2 * np.pi * freq * time + theta)

    phase_angle_start_next_wave = 2 * math.pi * freq * t_end + theta
    phase_angle_start_next_wave_normalized = math.fmod(phase_angle_start_next_wave, 2 * math.pi)

    # logger.warning("signal value at the end of the wave is: %.5f\n", sinewave[-1])
    # logger.warning("phase shift at the end of the wave is: %.5f\n", phase_angle_start_next_wave_normalized)

    theta = phase_angle_start_next_wave_normalized

    return sinewave

freq_new = 25

sinewave = generate_sinewave(freq = freq_new)

for i in range(4):
    freq_new += 10
    sinewave = np.concatenate((sinewave, generate_sinewave(freq = freq_new)))

fig = plt.Figure()
plt.title("Adding multiple sinusoids where frequency is incremented by 10")
plt.xlabel("Number of samples")
plt.ylabel("Amplitude")
plt.plot(sinewave)
plt.grid()
plt.show()