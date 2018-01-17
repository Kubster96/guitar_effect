from tkinter import *



def init(max_delay, max_repeats,max_volume,factor,
         default_delay=700,
         default_repeats=4,
         default_volume=1):
    master = Tk()
    master.title("Echo")

    scaleDict ={}

    delay = Scale(master, from_=0, to=max_delay,
              resolution=100,
              label="delay in ms",
              orient=HORIZONTAL,
              length=200)
    delay.grid(row=0, column=0, sticky=W)
    delay.set(default_delay)
    scaleDict['delay']=delay

    repeats = Scale(master, from_=1, to=max_repeats,
              label="number of repeats",
              orient=HORIZONTAL,
              length=200)
    repeats.grid(row=1, column=0, sticky=W)
    repeats.set(default_repeats)
    scaleDict['repeats']=repeats

    volume = Scale(master, from_=0, to=max_volume,
              resolution=0.1,
              label="volume",
              orient=HORIZONTAL,
              length=200)
    volume.grid(row=2, column=0, sticky=W)
    volume.set(default_volume)
    scaleDict['volume']=volume
    d = Scale(master, from_=20, to=-20, orient=HORIZONTAL)
    d.grid(row=3, column=0, sticky=W)
    d.set(factor)
    #eqList.append(d)
    return scaleDict


def start():
    mainloop()
