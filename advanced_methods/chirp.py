"""
This test will concatenate 3 sine waves, where the 1st chunk (sine wave) will have fixed frequency.
Second chunk will have a variable frequency from start till end. Last 3rd chunk is generated with fixed end frequency.
Base block of this test is a chirp signal that is implemented without using the library. Frequency is changed as a fcuntion of time,
while Amplitude is fixed the whole time. 
In order to avoid disconitnuities in the sine wave, phase tracking algorithm is implemented.  
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import chirp
import math
import logging

logger = logging.getLogger()

t_start = 0
t_end = 0.4
fs = 23500
nr_samples = int((t_end - t_start) * fs)
time = np.linspace(t_start, t_end, num = nr_samples)

start_freq = 1
end_freq = 50
theta = 0

def chirp_generator(Amp = 1, start_frequency = 1, end_frequency = 1, transition_time = 1):

    global theta

    k = (end_frequency - start_frequency) / transition_time # frequency change rate
    time = np.linspace(0, transition_time, num = int(transition_time*fs))
    chirp = Amp * np.sin(2 * math.pi * (k * time / 2 + start_frequency) * time + theta)

    phase_angle_start_next_wave = 2 * math.pi * (k * transition_time / 2 + start_frequency) * transition_time + theta
    phase_angle_start_next_wave_normalized = math.fmod(phase_angle_start_next_wave, 2 * math.pi)
    theta = phase_angle_start_next_wave_normalized

    # logger.warning("end phase: %.5f [deg], slope: %.5f\n", theta * 180 / math.pi, slope)
    # logger.warning("number of samples: %d\n")

    return chirp[:-1]

# 1st segment
t_end = 1 / start_freq
chirp = chirp_generator(start_frequency=start_freq, end_frequency=start_freq, transition_time=t_end)

# 2nd segment
chirp = np.concatenate((chirp, chirp_generator(start_frequency=start_freq, end_frequency=end_freq, transition_time=t_end)))

# 3rd segment
t_end = 1 / end_freq
chirp = np.concatenate((chirp, chirp_generator(start_frequency=end_freq, end_frequency=end_freq, transition_time=t_end)))

plt.plot(chirp)
plt.title("Sine wave with starting frequency " + str(start_freq) + " Hz and end frequency " + str(end_freq) + " Hz")
plt.xlabel("Number of samples")
plt.grid()
plt.show()

chirp_diff = np.gradient(chirp)
plt.plot(chirp_diff)
plt.title("1st derivative of the Sine wave with starting frequency " + str(start_freq) + " Hz and end frequency " + str(end_freq) + " Hz")
plt.xlabel("Number of samples")
plt.grid()
plt.show()