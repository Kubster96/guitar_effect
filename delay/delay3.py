import pyaudio
import time
import numpy as np
from copy import deepcopy


CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

samples = []
delay_time = 700
number_of_repeats = 4
samples_size = int((delay_time/1000) * number_of_repeats * RATE / 1024)
n = samples_size // number_of_repeats
index = 0


def main():
    global samples_size

    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=True,
                    stream_callback=delay_callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(60)
        stream.stop_stream()
    stream.close()

    p.terminate()


def delay_callback(in_data, frame_count, time_info, flag):
    global samples, index

    audio_data = np.fromstring(in_data, dtype=np.float32)
    copy = deepcopy(audio_data)

    i = len(samples) - n
    j = 0

    while i > 0:
        audio_data += samples[i]/(2**(j))
        i = i - n
        j = j + 1
    audio_data = audio_data/(j + 1)
    
    if index > samples_size:
        samples.pop(0)
        
    index = index + 1
    samples.append(copy)

    return audio_data, pyaudio.paContinue

main()
