# -*- coding: utf-8 -*-
"""Audio_signal_processing_for_machine_learning_#8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gu9B8ztJFcEWWidOXdkjRnTku-PWTOxj
"""

import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np

#load audio file
from google.colab import drive
drive.mount('/content/drive')

kick_sample = r"/content/drive/MyDrive/fileforcolab/Study/audio_signal_processing_for_machine_learning/#8/Kick Drum.wav"
voice_sample = r"/content/drive/MyDrive/fileforcolab/Study/audio_signal_processing_for_machine_learning/#8/Voice.wav"
music_sample = r"/content/drive/MyDrive/fileforcolab/Study/audio_signal_processing_for_machine_learning/#8/music.wav"

ipd.Audio(kick_sample)

ipd.Audio(voice_sample)

ipd.Audio(music_sample)

kick_sound, sr = librosa.load(kick_sample)
voice_sound, _ = librosa.load(voice_sample)
music_sound, _ = librosa.load(music_sample)

kick_sound

kick_sound.size

voice_sound.size

music_sound.size

# duration of 1 sample
print(sr)
sample_duration = 1 / sr
print(f"Duration of 1 sample is : {sample_duration:.6f} seconds")

# duration of the audio signal in seconds
# len() = sample 개수, len(sound) * ( 1 / sample rate ) 가 sound의 duration이 된다.
print(len(kick_sound))
duration = sample_duration * len(kick_sound)
print(f"Duration of signal is: {duration:.2f} seconds")

# visualise the waveforms

plt.figure(figsize=(15,17))

plt.subplot(3, 1, 1)
librosa.display.waveshow(music_sound, alpha =0.5)
plt.title("Music")
plt.ylim((-1,1))

plt.subplot(3, 1, 2)
librosa.display.waveshow(kick_sound, alpha =0.5)
plt.title("Kick")
plt.ylim((-1,1))


plt.subplot(3, 1, 3)
librosa.display.waveshow(voice_sound, alpha =0.5)
plt.title("Voice")
plt.ylim((-1,1))


plt.show()

# calculate the amplitude envelope
FRAME_SIZE = 1024
HOP_LENGTH = 512

def amplidude_envelope(signal, frame_size, hop_length):
  amplitude_envelope = []

  # calculate AE for each frame
  for i in range(0, len(signal), hop_length):
    current_frame_amplitude_envelope = max(signal[i:i+frame_size])
    amplitude_envelope.append(current_frame_amplitude_envelope)

  return np.array(amplitude_envelope)

def fancy_amplitude_envelope(signal, frame_size, hop_length):
  return np.array([max(signal[i:i+frame_size]) for i in range(0, signal.size, hop_length)])

ae_kick = amplidude_envelope(kick_sound, FRAME_SIZE, HOP_LENGTH)
len(ae_kick)|

fancy_ae_kick = fancy_amplitude_envelope(kick_sound, FRAME_SIZE, HOP_LENGTH)
len(fancy_ae_kick)

(ae_kick == fancy_ae_kick).all()

ae_kick = amplidude_envelope(kick_sound, FRAME_SIZE, HOP_LENGTH)
ae_voice = amplidude_envelope(voice_sound, FRAME_SIZE, HOP_LENGTH)
ae_music = amplidude_envelope(music_sound, FRAME_SIZE, HOP_LENGTH)

# visualise amplitude envelope for all the audio files

frames = range(0, ae_music.size)
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

plt.figure(figsize=(15,17))

plt.subplot(3, 1, 1)
librosa.display.waveshow(music_sound, alpha =0.5)
plt.plot(t, ae_music, color="r")
plt.title("Music")
plt.ylim((-1,1))

frames = range(0, ae_kick.size)
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

plt.subplot(3, 1, 2)
librosa.display.waveshow(kick_sound, alpha =0.5)
plt.plot(t, ae_kick, color="r")
plt.title("Kick")
plt.ylim((-1,1))

frames = range(0, ae_voice.size)
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)


plt.subplot(3, 1, 3)
librosa.display.waveshow(voice_sound, alpha =0.5)
plt.plot(t, ae_voice, color="r")
plt.title("Voice")
plt.ylim((-1,1))


plt.show()

|