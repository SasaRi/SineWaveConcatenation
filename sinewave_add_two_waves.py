import numpy as np
import matplotlib.pyplot as plt

theta = 0
t_start = 0
t_end = 0.08
fs = 13500
nr_samples = int((t_end - t_start) * fs)
time = np.linspace(t_start, t_end, num = nr_samples)

def generate_sinewave(Amp : float = 1, freq : float = 50):

    sinewave = Amp * np.sin(2 * np.pi * freq * time + theta)

    return sinewave

# test number 1; concatenate multiple sine waves with the same frequency
# result: since the previous segment always end at the phase 0 and new one starts at the 0 too, there are no discontinuities in the resulting signal  
Amp = 1
freq_new = 25

sinewave = generate_sinewave(freq = freq_new)

for i in range(4):
    Amp += 1
    sinewave = np.concatenate((sinewave, generate_sinewave(Amp = Amp, freq = freq_new)))

fig = plt.Figure()
plt.title("Adding multiple sinusoids with const. frequency of 25 Hz")
plt.xlabel("Number of samples")
plt.ylabel("Amplitude")
plt.plot(sinewave)
plt.grid()
plt.show()

# test number 2; change frequency and amplitude in every iteration 
# result: each segment (sine wave) doesn't end at the phase 0 (since sampling window is always constant and signal frequency changes)
#         since previous segment can end with phase != 0 and new segment starts with phase = 0, signal starts to show discontinuities  

freq_new = 25
Amp = 1

sinewave = generate_sinewave(freq = freq_new)

for i in range(4):
    freq_new += 10
    Amp += 1
    sinewave = np.concatenate((sinewave, generate_sinewave(Amp = Amp, freq = freq_new)))

fig = plt.Figure()
plt.title("Adding multiple sinusoids where frequency is incremented by 10 and amplitude by 1")
plt.xlabel("Number of samples")
plt.ylabel("Amplitude")
plt.plot(sinewave)
plt.grid()
plt.show()