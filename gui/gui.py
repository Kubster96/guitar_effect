
from tkinter import *


def show_values(eqList):
    for i in eqList:
        print(i.get())
    print()


eqList = []


master = Tk()
master.title("EQualizer")
a = Scale(master, from_=20, to=-20)
a.grid(row=0, column=0, sticky=W)
eqList.append(a)
b = Scale(master, from_=20, to=-20)
b.grid(row=0, column=1, sticky=W)
eqList.append(b)
c = Scale(master, from_=20, to=-20)
c.grid(row=0, column=2, sticky=W)
eqList.append(c)
d = Scale(master, from_=20, to=-20)
d.grid(row=0, column=3, sticky=W)
eqList.append(d)
e = Scale(master, from_=20, to=-20)
e.grid(row=0, column=4, sticky=W)
eqList.append(e)
Button(master, text='Show', command=lambda: show_values(eqList)).grid(row=1, column=2)
mainloop()
