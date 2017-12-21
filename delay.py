index = 0
samples = []
delay_time = 200
number_of_repeats = 3
samples_size = 0


def main():
    samples_size = (delay_time/1000) * number_of_repeats * RATE
    
    # reszta
    

def delay_callback(in_data, frame_count, time_info, flag):
    global samples, index

    n = int(delay_time/1000)*RATE

    audio_data = np.fromstring(in_data, dtype=np.float32)

    i = index % n

    while index > samples_size:
        for j in range(0, number_of_repeats):
            audio_data += samples[i+j*n]
        audio_data = audio_data/(number_of_repeats + 1)
        samples.pop(0)

    samples.append(audio_data)

    return audio_data, pyaudio.paContinue
