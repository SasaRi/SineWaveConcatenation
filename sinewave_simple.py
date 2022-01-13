import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig

t_start = 0
t_end = 0.08
fs = 13500
nr_samples = int((t_end - t_start) * fs)
time = np.linspace(t_start, t_end, num = nr_samples)

Amp = 1
f = 25
theta = 0
sinewave = Amp * np.sin(2 * np.pi * f * time + theta)

fig = plt.Figure()
plt.title("Sinusoid with frequency = 25 Hz")
plt.xlabel("Number of samples")
plt.ylabel("Amplitude")
plt.plot(sinewave)
plt.grid()
plt.show()