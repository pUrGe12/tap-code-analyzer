# can be used to input to a machine_learning algorithm

import librosa
import librosa.display as lbd
import numpy as np
import matplotlib.pylab as plt

path = 'C:\\Users\\hello\\Downloads\\test.wav'
raw_data, screen_rate = librosa.load(path)

num1 = 1
num2 = 1000000
freq_data = librosa.stft(raw_data[num1:num2]) # short time fourier transform to break into frequencies

sound_as_db = librosa.amplitude_to_db(np.abs(freq_data), ref = np.max)

# plotting
fig, ax = plt.subplots(figsize = (11,5))
img = lbd.specshow(sound_as_db, x_axis = 'time', y_axis = 'log', ax = ax)

ax.set_title('spectogram', fontsize = 20)
fig.colorbar(img, ax=ax, format = f'%0.2f')
plt.show()
