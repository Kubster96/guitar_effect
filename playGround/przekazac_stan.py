import time

import numpy as np
import pyaudio
import scipy.signal as signal

CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])
counter = 0
DROP_FIRST = 3
buffer = []
z =None
counter =0

def main():
    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(100)
        stream.stop_stream()
    stream.close()

    p.terminate()



# def callback(in_data, frame_count, time_info, flag):
#     global z,counter
#
#     audio_data = np.fromstring(in_data, dtype=np.float32) / 5
#     x = None
#     if counter < DROP_FIRST:
#         buffer.append(butter_bandpass_filter(audio_data, 512, 1024, RATE))
#     else:
#         buffer.append(audio_data)
#         x,zi = butter_bandpass_filter_zi(np.concatenate(buffer), 512, 1024, RATE,z)[(len(buffer)-3)*1024:]
#         z=zi
#         buffer.pop(0)
#         if counter > 100:
#             plt.plot(np.linspace(0, 1, 3*frame_count), x)
#             plt.show()
#     counter += 1
#
#     return audio_data, pyaudio.paContinue
#

def callback(in_data, frame_count, time_info, flag):
    global z
    audio_data = np.fromstring(in_data, dtype=np.float32) / 5

    # x,zi = butter_bandpass_filter_zi(audio_data, 512, 1024, RATE,z)
    # z=zi
    nyq = 0.5 * RATE
    high = 1024 / nyq
    # low = 100 / nyq
    b,a = signal.butter(5, high, 'high', analog=False)
    if z is None:
        z =signal.lfilter_zi(b,a)
    filtered = signal.filtfilt(b,a,audio_data,padlen=50)
    # z=zi

    return filtered, pyaudio.paContinue
main()
5