import numpy as np
import matplotlib.pyplot as plt
import math
import logging

logger = logging.getLogger()

t_start = 0
t_end = 0.4
fs = 23500
nr_samples = int((t_end - t_start) * fs)

theta = 0

# this generator will be based on a chirp signal (both frequency and amplitude will be functions of time)
# transition time is universal for both frequency and amplitude (transition time of amplitude = transition time of frequency)
# transition time is user configured and defines the duration of one chunk 
def sinewave_generator(Amp_start, Amp_final = 1, Freq_start = 1, Freq_end = 1, transition_time = 1):
    global theta

    # time interval spans from 0 to configured transition time 
    time = np.linspace(0, transition_time, num = int(transition_time * fs))

    # frequency change rate
    freq_rate = (Freq_end - Freq_start) / transition_time

    # amplitude change rate
    k = (Amp_final - Amp_start) / transition_time
    Amp = k * time + Amp_start
    
    # resulting signal
    signal = Amp * np.sin(2 * math.pi * (freq_rate * time / 2 + Freq_start) * time + theta)

    # phase shift tracking (calculate normalized value of the phase angle at the end of the chunk)
    phase_angle_start_next_wave = 2 * math.pi * (freq_rate * transition_time / 2 + Freq_start) * transition_time + theta
    phase_angle_start_next_wave_normalized = math.fmod(phase_angle_start_next_wave, 2 * math.pi)
    theta = phase_angle_start_next_wave_normalized

    return signal[:-1]


# main application
AMPLITUDE_0 = 1
AMPLITUDE_1 = 10
FREQUENCY_0 = 1
FREQUENCY_1 = 10

# 1st chunk (sinewave)
sinewave = sinewave_generator(Amp_start=AMPLITUDE_0, Amp_final=AMPLITUDE_0, Freq_start=FREQUENCY_0, Freq_end=FREQUENCY_0, transition_time=1/FREQUENCY_0)

# add 2nd chunk with changing both frequency and amplitude to the end values as function of time
sinewave = np.concatenate((sinewave, sinewave_generator(Amp_start=AMPLITUDE_0, Amp_final=AMPLITUDE_1, \
    Freq_start=FREQUENCY_0, Freq_end=FREQUENCY_1, transition_time=1/FREQUENCY_0)))

# add final chunk with fixed end amplitude and frequency
sinewave = np.concatenate((sinewave, sinewave_generator(Amp_start=AMPLITUDE_1, Amp_final=AMPLITUDE_1, \
    Freq_start=FREQUENCY_1, Freq_end=FREQUENCY_1, transition_time=1/FREQUENCY_1)))

plt.plot(sinewave)
plt.title("Sinewave based on chirp signal, both amplitude and frequency are functions of time")
plt.xlabel("Number of samples")
plt.grid()
plt.show()

sinewave_diff = np.gradient(sinewave)
plt.plot(sinewave_diff)
plt.title(" 1st derivative Sinewave based on chirp signal, both amplitude and frequency are functions of time")
plt.xlabel("Number of samples")
plt.grid()
plt.show()