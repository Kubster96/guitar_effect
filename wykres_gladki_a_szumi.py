import pyaudio
import time
import numpy as np
from butter_transform import butter_bandpass_filter, transform
from matplotlib import pyplot as plt
import scipy.signal as signal

CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])
counter = 0
DROP_FIRST = 3
buffer = []


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

    p.terminate()


def callback2(in_data, frame_count, time_info, flag):
    global b, a, fulldata  # global variables for filter coefficients and array
    audio_data = np.fromstring(in_data, dtype=np.float32)
    # do whatever with data, in my case I want to hear my data filtered in realtime
    # audio_data = signal.filtfilt(b, a, audio_data, padlen=200).astype(np.float32).tostring()
    fulldata = np.append(fulldata, audio_data)
    # saves filtered data in an array
    return audio_data, pyaudio.paContinue


def callback(in_data, frame_count, time_info, flag):
    global b, a, fulldata, dry_data, counter
    audio_data = np.fromstring(in_data, dtype=np.float32) / 5
    x = None
    if counter < DROP_FIRST:
        buffer.append(butter_bandpass_filter(audio_data, 512, 1024, RATE))
    else:
        buffer.append(audio_data)
        x = butter_bandpass_filter(np.concatenate(buffer), 512, 1024, RATE)[(len(buffer)-3)*1024:]
        buffer.pop(0)
        if counter > 100:
            # plt.plot(np.linspace(0, 1, frame_count), audio_data)
            # plt.show()
            plt.plot(np.linspace(0, 1, 3*frame_count), x)
            plt.show()



    counter += 1

    return audio_data, pyaudio.paContinue


main()
