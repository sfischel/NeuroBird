# -*- coding: utf-8 -*-
"""UPDATED Data Preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14z3WU1ePNLXkUijDQx6uzyZmMVw9dBnK
"""

!pip install mne
import mne
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from mne import create_info
from mne.io import RawArray

path = r"/content/anthony Trial B (r) 3.txt"

df = pd.read_csv(path, delimiter = ',', skiprows=4)
data = df.to_numpy()
data = np.delete(data, [0,2,3,4,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24] ,axis=1)
data = data[:, :-1]
sorted_indices = np.argsort(data[:, 0])
data = data.T

# Sample Index, EXG Channel 0, EXG Channel 1, EXG Channel 2, EXG Channel 3, EXG Channel 4, EXG Channel 5, EXG Channel 6, EXG Channel 7, Accel Channel 0, Accel Channel 1, Accel Channel 2, Other, Other, Other, Other, Other, Other, Other, Analog Channel 0, Analog Channel 1, Analog Channel 2, Timestamp, Other, Timestamp (Formatted)
# 0 132.0,
# 1 36596.82412109663,
# 2 0.0,
# 3 0.0,
# 4 0.0,
# 5 47023.51057809718,
# 6 82606.52662593445,
# 7-11 0.0, 0.0, 0.0, 0.0, 0.0,
# 12 192.0,
# 13-24 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.7088279234137409E9, 0.0, 2024-02-24 18:25:23.413

print(data.shape)
ch_types = [ 'eeg', 'eeg', 'eeg']
ch_names = [ 'CP5', 'FC5', 'C3']
sfreq = 250
info = mne.create_info (ch_names = ch_names, sfreq = sfreq, ch_types = ch_types)
raw = mne.io.RawArray (data, info)
raw.plot_psd(fmax=15, color="blue") # plot data, truncate x axis at 15
plt.savefig ('psd.png')

# Apply a low-pass filter with a cutoff frequency of 40 Hz
raw.filter(l_freq=4.5, h_freq=5.5)

raw.plot(scalings='auto');
raw.plot_psd(fmin=2, fmax=10);