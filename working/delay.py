import pyaudio
import numpy as np
from copy import deepcopy

import gui as myGui

CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

samples = []

max_delay = 2500
max_repeats = 5
max_volume = 5
max_volume_drop=5

gui = myGui.init(max_delay, max_repeats, max_volume, max_volume_drop)

max_sample_size = int((max_delay / 1000) * max_repeats * RATE / 1024)

delay = 500
number_of_repeats = 4
samples_size = int((delay / 1000) * number_of_repeats * RATE / 1024)
single_sample_size = samples_size // number_of_repeats
index = 0


def update():
    global delay, number_of_repeats, samples_size, single_sample_size
    delay = gui['delay'].get()
    number_of_repeats = gui['repeats'].get()
    samples_size = int((delay / 1000) * number_of_repeats * RATE / 1024)
    single_sample_size = samples_size // number_of_repeats


def main():
    global max_sample_size

    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=True,
                    stream_callback=delay_callback)

    stream.start_stream()

    while stream.is_active():
        myGui.start()
        stream.stop_stream()
    stream.close()

    p.terminate()


def delay_callback(in_data, frame_count, time_info, flag):
    global samples, index
    update()
    audio_data = np.fromstring(in_data, dtype=np.float32) * 5 * gui['volume'].get()
    if delay == 0:
        samples.append(audio_data)
        return audio_data, pyaudio.paContinue
    copy = deepcopy(audio_data)
    i = len(samples) - single_sample_size
    j = 0

    while i > 0 and j < number_of_repeats:
        audio_data += samples[i] / (gui['volume_drop'].get() * j + 1)
        i = i - single_sample_size
        j = j + 1
    audio_data = audio_data / (j + 1)

    if index > max_sample_size:
        samples.pop(0)

    index = index + 1
    samples.append(copy)

    return audio_data, pyaudio.paContinue


main()

