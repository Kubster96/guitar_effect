from tkinter import *


def init(max_delay, max_repeats, max_volume, max_drop,
         default_delay=700,
         default_repeats=4,
         default_volume=1,
         default_drop =2):
    master = Tk()
    master.title("Echo")

    scale_dict = {}

    delay = Scale(master, from_=0, to=max_delay,
                  resolution=100,
                  label="delay in ms",
                  orient=HORIZONTAL,
                  length=200)
    delay.grid(row=0, column=0, sticky=W)
    delay.set(default_delay)
    scale_dict['delay'] = delay

    repeats = Scale(master, from_=1, to=max_repeats,
                    label="number of repeats",
                    orient=HORIZONTAL,
                    length=200)
    repeats.grid(row=1, column=0, sticky=W)
    repeats.set(default_repeats)
    scale_dict['repeats'] = repeats

    volume = Scale(master, from_=0, to=max_volume,
                   resolution=0.1,
                   label="volume",
                   orient=HORIZONTAL,
                   length=200)
    volume.grid(row=2, column=0, sticky=W)
    volume.set(default_volume)
    scale_dict['volume'] = volume
    volume_drop = Scale(master, from_=0, to=max_drop,
                        label='volume drop speed',
                        orient=HORIZONTAL,
                        length=200)
    volume_drop.grid(row=3, column=0, sticky=W)
    volume_drop.set(default_drop)
    scale_dict['volume_drop'] = volume_drop
    return scale_dict


def start():
    mainloop()
