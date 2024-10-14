import numpy as np
from pvrecorder import PvRecorder
from pydub import AudioSegment
import wave
import struct
import keyboard

def audio_file_to_signal(file_path):
    """
    Converts an audio file to a signal (raw audio data) and retrieves the frame rate.
    Args:
        file_path (str): The path to the audio file. Supports formats like MP3, WAV, etc.
    Returns:
        tuple: A tuple containing:
            - samples (numpy.ndarray): The raw audio data as a NumPy array. If the audio is stereo, the array is reshaped accordingly.
            - frame_rate (int): The frame rate (sampling rate) of the audio.
    """
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
def record_audio():
    """
    Records audio using the PvRecorder and saves it to a WAV file.
    This function initializes the PvRecorder with a specified device index and frame length.
    It starts recording audio and appends the recorded frames to a list until a KeyboardInterrupt
    (Ctrl+C) is detected. Upon stopping the recording, it writes the recorded audio to a WAV file
    named 'output_record.wav' in the 'sample_voice' directory.
    Raises:
        KeyboardInterrupt: If the recording is manually stopped by the user.
    Note:
        Ensure that the 'sample_voice' directory exists before running this function.
    """
    recorder = PvRecorder(device_index=-1, frame_length=512)
    audio = []

    try:
        while True:
            recorder.start()
            print("Recording... Press Ctrl+C to stop or 'r' to erase and redo.")
            audio = []  # Clear audio list every time recording starts
            while True:
                if keyboard.is_pressed('r'):  # Check if 'r' is pressed for redo
                    print("Redo recording...")
                    recorder.stop()
                    break  # Exit the loop and restart recording
                frame = recorder.read()
                audio.extend(frame)
    except KeyboardInterrupt:
        # This will catch Ctrl+C
        recorder.stop()
        print("Recording stopped.")
        # Save the audio file
        with wave.open('sample_voice/output_record.wav', 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
    finally:
        recorder.delete()