from audio_manage import audio_file_to_signal, record_audio
from visualization_manage import plot_waveform

if __name__ == "__main__":
    # Path to your audio file (MP3 or WAV)
    record_audio()

    audio_file = "sample_voice/output_record.mp3" 
    # Get the audio signal and frame rate
    signal, rate = audio_file_to_signal(audio_file)
    
    # Plot the waveform
    plot_waveform(signal, rate)