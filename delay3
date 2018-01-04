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
delay_time = 3999
number_of_repeats = 4
samples_size = int((delay_time/1000) * number_of_repeats * RATE / 1024)
n = samples_size //number_of_repeats

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

        #for j in range(0, number_of_repeats):
        #    audio_data += samples[j*n] /(2**(number_of_repeats -j))
        #audio_data = audio_data/(number_of_repeats + 1)
        
    index = index + 1
    samples.append(copy)

    return audio_data, pyaudio.paContinue


main()
