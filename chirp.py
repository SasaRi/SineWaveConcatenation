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

start_freq = 2.5
end_freq = 10
theta = 0

# implement chirp signal without using the library
def chirp_generator(Amp = 1, start_frequency = 1, end_frequency = 1, transition_time = 1):

    global theta

    k = (end_frequency - start_frequency) / transition_time # frequency change rate
    time = np.linspace(0, transition_time, num = int(transition_time*fs))
    chirp = Amp * np.sin(2 * math.pi * (k * time / 2 + start_frequency) * time + theta)

    phase_angle_start_next_wave = 2 * math.pi * (k * transition_time / 2 + start_frequency) * transition_time + theta
    phase_angle_start_next_wave_normalized = math.fmod(phase_angle_start_next_wave, 2 * math.pi)
    theta = phase_angle_start_next_wave_normalized

    slope = chirp[-2] - chirp[-1]

    # logger.warning("end phase: %.5f [deg], slope: %.5f\n", theta * 180 / math.pi, slope)
    # logger.warning("number of samples: %d\n")

    return chirp[:-1]

# chiro = chirp(time, f0=start_freq, t1=3*(t_end-t_start)/2, f1=end_freq, method="linear")
# plt.plot(chirp)
# plt.title("Chirp signal")
# plt.xlabel("Number of samples")
# plt.grid()
# plt.show()

# 1st segment
t_end = 1 / start_freq
chirp = chirp_generator(start_frequency=start_freq, end_frequency=start_freq, transition_time=t_end)

# 2nd segment
chirp = np.concatenate((chirp, chirp_generator(start_frequency=start_freq, end_frequency=end_freq, transition_time=t_end)))

# 3rd segment
t_end = 1 / end_freq
chirp = np.concatenate((chirp, chirp_generator(start_frequency=end_freq, end_frequency=end_freq, transition_time=t_end)))

plt.plot(chirp)
plt.title("Chirp signal")
plt.xlabel("Number of samples")
plt.grid()
plt.show()

chirp_diff = np.gradient(chirp)
plt.plot(chirp_diff)
plt.title("Chirp signal, 1st derivative")
plt.xlabel("Number of samples")
plt.grid()
plt.show()