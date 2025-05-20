#Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
from pydub import AudioSegment

#Load mp3 and export as wav
sound = AudioSegment.from_mp3("SoundHelix-Song-1.mp3")
sound.export("sample_audio.wav", format="wav")

#Read audiodata from wavfile package
samplerate, data = wavfile.read("sample_audio.wav")

#Create timeline
duration = len(data) / samplerate
time = np.linspace(0., duration, len(data))

#Plot audiosignal
plt.figure(figsize=(10,4))
plt.plot(time, data)
plt.title("Audiosignal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

#Fourier_Transformation
N = len(data)
yf = fft(data)
xf = np.linspace(0.0, samplerate / 2.0, N // 2)

#Plot frequency spectrum
plt.figure(figsize=(10,4))
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.title("Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()