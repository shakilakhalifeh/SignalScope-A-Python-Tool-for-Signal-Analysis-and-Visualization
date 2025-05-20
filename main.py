#Import libraries
import matplotlib.pyplot as plt
from signal_analysis import generate_signal, compute_fft, low_pass_filter

#Parameters
sampling_rate = 1000
duration = 2
freq = 5

#Generate signal
t, noisy_signal = generate_signal(freq=freq, noise_level=0.5, duration=duration)

#Filter signal
filtered_signal = low_pass_filter(noisy_signal, cutoff=10, sampling_rate=sampling_rate)

#Fast Fouriour Transform
xf, yf = compute_fft(noisy_signal, sampling_rate)
xf_filt, yf_filt = compute_fft(filtered_signal, sampling_rate)

# Plot time domain
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, noisy_signal, label="Noisy Signal")
plt.plot(t, filtered_signal, label="Filtered Signal")
plt.xlabel("Time [s]")
plt.title("Time Domain")
plt.legend()

#Plot frequency domain
plt.subplot(1, 2, 2)
plt.plot(xf, yf, label="Original FFT")
plt.plot(xf_filt, yf_filt, label="Filtered FFT")
plt.xlabel("Frequency [Hz]")
plt.title("Frequency Domain")
plt.legend()

plt.tight_layout()
plt.show()