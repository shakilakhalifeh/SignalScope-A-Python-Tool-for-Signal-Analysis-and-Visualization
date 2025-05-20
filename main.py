#Import libraries
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import butter, filtfilt

#Create functions: generate_signal(), compute_fft(), and low_pass_filter()
def generate_signal(freq=5, noise_level=0.5, duration=2, sampling_rate=1000):
    t = np.linspace(0, durarion, int(sampling_rate * duration))
    clean_signal = np.sin(2 * np.pi * freq * t)
    noise = noise_level * np.random.randn(len(t))
    signal = clean_signal + noise
    return t, signal


def compute_fft(signal, sampling_rate):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / sampling_rate)
    return xf[:N//2], np.abs(yf[:N//2])

def low_pass_filter(signal, cutoff, sampling_rate, order=5):
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype="low", analog=False)
    return filtfilt(b, a, signal)