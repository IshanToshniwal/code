from tkinter import *

t = Tk()


def ENTRY_OF_CHILD():
    L1 = Label(t, text='Name =')
    L2 = Label(t)
    L2.grid(row=2)
    L1.grid(row=3, column=1)
    E1 = Entry(t)
    E1.grid(row=3, column=2)


ENTRY_OF_CHILD()
t.mainloop()
