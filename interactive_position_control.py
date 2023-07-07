from braccio import Braccio
import sys
import time
from tkinter import *

if len(sys.argv) < 2:
    raise ValueError("Missing parameters: <arduino_port>")

arm = Braccio(sys.argv[1])
arm.home()

root = tk.Tk()
tk.Label(root, text="X").grid(row=0)
tk.Label(root, text="Y").grid(row=1)
x = tk.Entry(root)
y = tk.Entry(root)
x.grid(row=0, column=1)
y.grid(row=1, column=1)


def go():
    pass


Button(root, text='Write', command=go).pack()
root.mainloop()
