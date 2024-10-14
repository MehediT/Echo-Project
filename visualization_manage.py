import matplotlib.pyplot as plt
import numpy as np


def plot_waveform(signal, rate):
    """
    Plots the waveform of an audio signal.
    Parameters:
    signal (numpy.ndarray): The audio signal data.
    rate (int): The frame rate (samples per second) of the audio signal.
    Returns:
    None
    """
    # Create a time axis based on the frame rate and length of the signal
    time_axis = np.linspace(0, len(signal) / rate, num=len(signal))

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, signal)
    plt.title("Audio Signal Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.show()