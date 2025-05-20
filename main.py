{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3ed83ee8-113a-4fcb-971e-692276933cdd",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'signal_analysis'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mplt\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msignal_analysis\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m generate_signal, compute_fft, low_pass_filter\n\u001b[1;32m      4\u001b[0m \u001b[38;5;66;03m#Parameters\u001b[39;00m\n\u001b[1;32m      5\u001b[0m sampling_rate \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1000\u001b[39m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'signal_analysis'"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from signal_analysis import generate_signal, compute_fft, low_pass_filter\n",
    "\n",
    "#Parameters\n",
    "sampling_rate = 1000\n",
    "duration = 2\n",
    "freq = 5\n",
    "\n",
    "#Generate signal\n",
    "t, noisy_signal = generate_signal(freq=freq, noise_level=0.5, duration=duration)\n",
    "\n",
    "#Filter signal\n",
    "filtered_signal = low_pass_filter(noisy_signal, cutoff=10, sampling_rate=sampling_rate)\n",
    "\n",
    "#Fast Fouriour Transform\n",
    "xf, yf = compute_fft(noisy_signal, sampling_rate)\n",
    "xf_filt, yf_filt = compute_fft(filtered_signal, sampling_rate)\n",
    "\n",
    "# Plot time domain\n",
    "plt.figure(figsize=(12, 5))\n",
    "plt.subplot(1, 2, 1)\n",
    "plt.plot(t, noisy_signal, label=\"Noisy Signal\")\n",
    "plt.plot(t, filtered_signal, label=\"Filtered Signal\")\n",
    "plt.xlabel(\"Time [s]\")\n",
    "plt.title(\"Time Domain\")\n",
    "plt.legend()\n",
    "\n",
    "#Plot frequency domain\n",
    "plt.subplot(1, 2, 2)\n",
    "plt.plot(xf, yf, label=\"Original FFT\")\n",
    "plt.plot(xf_filt, yf_filt, label=\"Filtered FFT\")\n",
    "plt.xlabel(\"Frequency [Hz]\")\n",
    "plt.title(\"Frequency Domain\")\n",
    "plt.legend()\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
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
