import serial
import time
import solverNNA
import numpy as np

# sudo chmod 777 /dev/ttyACM0
arm = serial.Serial('/dev/ttyACM0', 115200, timeout=5)

axis_names = ["base", "shoulder", "elbow", "wrist", "wristRot", "gripper"]
home_angles = [0,150,0,0,90,73]
min_max_angles = [(0,180), (15,165), (0,180), (0,180), (0,180), (0, 73)]

def clamp(value, bounds):
    if value < bounds[0]:
        return bounds[0]
    if value > bounds[1]:
        return bounds[1]
    return value

def wait_and_handle_ack():
    response = arm.readline().decode().strip()
    if response == "OK":
        return
    print("ERROR: '{}'".format(response))

def write_angles(angles, speed=20):
    angles = [clamp(angle, angle_bounds) for (angle, angle_bounds) in zip(angles, min_max_angles)]
    angle_string="P {angles} {speed}\n".format(angles=' '.join([str(elem) for elem in angles]), speed=speed)
    arm.write(angle_string.encode())
    arm.flush()
    wait_and_handle_ack()

def home(speed=20):
    write_angles(home_angles, speed)

print("Initializing arm")
time.sleep(2) # wait for the arduino to wake up
arm.readlines() # empty the input buffer

home()
home()
