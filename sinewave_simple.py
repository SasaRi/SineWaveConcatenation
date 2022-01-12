import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig

t_start = 0
t_end = 0.08
fs = 13500
time = np.arange(t_start, t_end, 1 / fs)

Amp = 1
f = 25
theta = 0
sinewave = Amp * np.sin(2 * np.pi * f * time + theta)

fig.Figure()
plt.plot(sinewave)
plt.grid()
plt.show()