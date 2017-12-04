# import pyaudio
# import numpy as np
#
# RATE = 44100
# CHUNK = 1024
#
# p = pyaudio.PyAudio()
#
# player = p.open(format=pyaudio.paInt16, channels=2, rate=RATE, output=True, frames_per_buffer=CHUNK)
# stream = p.open(format=pyaudio.paInt16, channels=2, rate=RATE, input=True, frames_per_buffer=CHUNK)
#
# for i in range(int(20*RATE/CHUNK)):
#     player.write(np.fromstring(stream.read(CHUNK), dtype=np.int16), CHUNK)
#
# stream.stop_stream()
# stream.close()
# p.terminate()

import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as signal

CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])
# b, a = signal.iirdesign(0.03, 0.07, 5, 40)


def main():
    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(10)
        stream.stop_stream()
    stream.close()

    # numpydata = np.hstack(fulldata)
    # plt.plot(numpydata)
    # plt.title("Wet")
    # plt.show()
    #
    #
    # numpydata = np.hstack(dry_data)
    # plt.plot(numpydata)
    # plt.title("Dry")
    # plt.show()

    p.terminate()


def callback2(in_data, frame_count, time_info, flag):
    global b,a,fulldata #global variables for filter coefficients and array
    audio_data = np.fromstring(in_data, dtype=np.float32)
    # do whatever with data, in my case I want to hear my data filtered in realtime
    # audio_data = signal.filtfilt(b, a, audio_data, padlen=200).astype(np.float32).tostring()
    fulldata = np.append(fulldata,audio_data)
    # saves filtered data in an array
    return audio_data, pyaudio.paContinue


def callback(in_data, frame_count, time_info, flag):
    global b, a, fulldata, dry_data,frames
    audio_data = np.fromstring(in_data, dtype=np.float32)/10
    dry_data = np.append(dry_data,audio_data)

    # do processing here
    fulldata = np.append(fulldata,audio_data)
    return audio_data , pyaudio.paContinue

main()
