{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e6477c6c-cf15-4e0d-8116-f5635764ce14",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import libraries\n",
    "import numpy as np\n",
    "from scipy.fft import fft, fftfreq\n",
    "from scipy.signal import butter, filtfilt\n",
    "\n",
    "#Create functions: generate_signal(), compute_fft(), and low_pass_filter()\n",
    "def generate_signal(freq=5, noise_level=0.5, duration=2, sampling_rate=1000):\n",
    "    t = np.linspace(0, durarion, int(sampling_rate * duration))\n",
    "    clean_signal = np.sin(2 * np.pi * freq * t)\n",
    "    noise = noise_level * np.random.randn(len(t))\n",
    "    signal = clean_signal + noise\n",
    "    return t, signal\n",
    "\n",
    "\n",
    "def compute_fft(signal, sampling_rate):\n",
    "    N = len(signal)\n",
    "    yf = fft(signal)\n",
    "    xf = fftfreq(N, 1 / sampling_rate)\n",
    "    return xf[:N//2], np.abs(yf[:N//2])\n",
    "\n",
    "def low_pass_filter(signal, cutoff, sampling_rate, order=5):\n",
    "    nyquist = 0.5 * sampling_rate\n",
    "    normal_cutoff = cutoff / nyquist\n",
    "    b, a = butter(order, normal_cutoff, btype=\"low\", analog=False)\n",
    "    return filtfilt(b, a, signal)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
