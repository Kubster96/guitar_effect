import pyaudio
import time
import numpy as np
from copy import deepcopy
from butter_transform import butter_bandpass_filter, transform
from matplotlib import pyplot as plt
import scipy.signal as signal

CHANNELS = 1
RATE = 44100

r=0

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])
counter = 0
DROP_FIRST = 3
first = 44100
index = 0

samples = []
delay_time = 200
number_of_repeats = 3
samples_size = 0


def main():
    global samples_size

    samples_size = int((delay_time/1000) * number_of_repeats * RATE // 1024)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=True,
                    stream_callback=delay_callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(20)
        stream.stop_stream()
    stream.close()

    p.terminate()


def delay_callback(in_data, frame_count, time_info, flag):
    global samples, index

    n = int((delay_time/1000)*RATE//1024)
    # n to jest ile elementow ma jeden przedzial

    audio_data = np.fromstring(in_data, dtype=np.float32)
    copy = deepcopy(audio_data)

    while index > samples_size:

        print(len(samples))
        print(n)
        print()

        for j in range(0, number_of_repeats):
            audio_data += samples[j*n]
        audio_data = audio_data/(number_of_repeats + 1)
        samples.pop(0)

    index = index + 1
    samples.append(copy)

    return audio_data, pyaudio.paContinue


main()
