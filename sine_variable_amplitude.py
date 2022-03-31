import numpy as np
import matplotlib.pyplot as plt

theta = 0
t_start = 0
t_end = 0.08
fs = 13500
freq = 25
nr_samples = int((t_end - t_start) * fs)

STARTING_AMPLITUDE = 1 # Hz
ENDING_AMPLITUDE = 100 # Hz

initial_Amplitude = STARTING_AMPLITUDE

def generate_sinewave(end_Amplitude = 1, transition_time = 1, freq = 1, theta = 0):

    global initial_Amplitude

    k = (end_Amplitude - initial_Amplitude) / transition_time
    time = np.linspace(0, transition_time, num = int(transition_time*fs))
    Amp = k * time + initial_Amplitude

    sinewave = Amp * np.sin(2 * np.pi * freq * time + theta)

    initial_Amplitude = Amp[-1]

    return sinewave[:-1]

# 1st segment
sine_wave = generate_sinewave(end_Amplitude=STARTING_AMPLITUDE, transition_time=t_end, freq=freq)

# 2nd segment
sine_wave = np.concatenate((sine_wave, generate_sinewave(end_Amplitude=ENDING_AMPLITUDE, transition_time=t_end, freq=freq)))

# 3rd segment
chirp = np.concatenate((sine_wave, generate_sinewave(end_Amplitude=ENDING_AMPLITUDE, transition_time=t_end, freq=freq)))

plt.plot(chirp)
plt.title("Sine wave with variable amplitude")
plt.xlabel("Number of samples")
plt.grid()
plt.show()

sinewave_diff = np.gradient(chirp)
plt.plot(sinewave_diff)
plt.title("Sine wave with variable amplitude, 1st derivative")
plt.xlabel("Number of samples")
plt.grid()
plt.show()