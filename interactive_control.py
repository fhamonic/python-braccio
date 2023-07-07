from braccio import Braccio
import cv2
import sys
import time
from tkinter import *

if len(sys.argv) < 2:
    raise ValueError("Missing parameters: <arduino_port>")

arm = Braccio(sys.argv[1])

arm.home()

def write_angle():
    arm.move_to([base_angle.get(), shoulder_angle.get(), elbow_angle.get(),
                wrist_angle.get(), wristRot_angle.get(), gripper_angle.get()], speed.get())

def reset_angles():
    base_angle.set(0)
    shoulder_angle.set(90)
    elbow_angle.set(90)
    wrist_angle.set(90)
    wristRot_angle.set(90)
    gripper_angle.set(90)
    write_angles.set(0)

master = Tk()
base_angle = Scale(master, from_=0, to=180, orient=HORIZONTAL)
base_angle.pack()
shoulder_angle = Scale(master, from_=15, to=165, orient=HORIZONTAL)
shoulder_angle.pack()
elbow_angle = Scale(master, from_=0, to=180, orient=HORIZONTAL)
elbow_angle.pack()
wrist_angle = Scale(master, from_=0, to=180, orient=HORIZONTAL)
wrist_angle.pack()
wristRot_angle = Scale(master, from_=0, to=180, orient=HORIZONTAL)
wristRot_angle.pack()
gripper_angle = Scale(master, from_=0, to=73, orient=HORIZONTAL)
gripper_angle.pack()
speed = Scale(master, from_=0, to=200, orient=HORIZONTAL)
speed.pack()

Button(master, text='Reset', command=reset_angles).pack()
Button(master, text='Write', command=write_angle).pack()

mainloop()
