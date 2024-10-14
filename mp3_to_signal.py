from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

def mp3_to_signal(file_path):
    # Load the MP3 file
    audio = AudioSegment.from_file(file_path)  # Supports MP3, WAV, etc.

    # Convert to raw audio data (samples)
    samples = np.array(audio.get_array_of_samples())

    # Handle stereo files by reshaping
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))

    # Get the frame rate (sampling rate) of the audio
    frame_rate = audio.frame_rate

    return samples, frame_rate

def plot_waveform(signal, rate):
    # Create a time axis based on the frame rate and length of the signal
    time_axis = np.linspace(0, len(signal) / rate, num=len(signal))

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, signal)
    plt.title("Audio Signal Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.show()

if __name__ == "__main__":
    # Path to your audio file (MP3 or WAV)
    audio_file = "sample_voice/rouge.mp3"  # Replace with your file path
    
    # Get the audio signal and frame rate
    signal, rate = mp3_to_signal(audio_file)
    
    # Plot the waveform
    plot_waveform(signal, rate)
