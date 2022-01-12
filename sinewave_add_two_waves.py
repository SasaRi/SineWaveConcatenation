import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig

theta = 0
t_start = 0
t_end = 0.08
fs = 13500
time = np.arange(t_start, t_end, 1 / fs)

def generate_sinewave(Amp : float = 1, freq : float = 50):

    sinewave = Amp * np.sin(2 * np.pi * freq * time + theta)

    return sinewave

# test number 1; concatenate multiple sine waves with the same frequency
# result: since the previous segment always end at the phase 0 and new one starts at the 0 too, there are no discontinuities in the resulting signal  
freq_new = 25

sinewave = generate_sinewave(freq = freq_new)

for i in range(4):
    sinewave = np.concatenate((sinewave, generate_sinewave(freq = freq_new)))

fig.Figure()
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

fig.Figure()
plt.plot(sinewave)
plt.grid()
plt.show()