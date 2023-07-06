import serial
import time
import numpy as np

# sudo chmod 777 /dev/ttyACM0
arm = serial.Serial('/dev/ttyACM0', 115200, timeout=5)
axis_names = ["base", "shoulder", "elbow", "wrist", "wristRot", "gripper"]
min_max_angles = [(0, 180), (15, 165), (0, 180), (0, 180), (0, 180), (0, 73)]


def init():
    print("INIT")
    arm.readlines()  # wait for the arduino to wake up and empty the input buffer


def wait_and_handle_ack():
    response = arm.readline().decode().strip()
    if response != "OK":
        raise Exception("Arduino responded: '{}'".format(response))


def power_on():
    print("POWER_ON")
    arm.write("1\n".encode())
    wait_and_handle_ack()


def power_off():
    print("POWER_OFF")
    arm.write("0\n".encode())
    wait_and_handle_ack()


def clamp_value(value, bounds):
    if value < bounds[0]:
        return bounds[0]
    if value > bounds[1]:
        return bounds[1]
    return value


def move_to(angles, speed=20):
    print("MOVE_TO {} {}".format(angles, speed))
    angles = [clamp_value(angle, angle_bounds)
              for (angle, angle_bounds) in zip(angles, min_max_angles)]
    angle_string = "P {angles} {speed}\n".format(
        angles=' '.join([str(elem) for elem in angles]), speed=speed)
    arm.write(angle_string.encode())
    wait_and_handle_ack()


def home(speed=20):
    print("HOME")
    home_angles = [0, 150, 0, 0, 90, 73]
    move_to(home_angles, speed)


def shutdown(speed=50):
    print("SHUTDOWN")
    shutdown_angles = [0, 70, 20, 20, 90, 0]
    move_to(shutdown_angles, speed)
    power_off()

init()
shutdown()
