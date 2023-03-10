#!/bin/python3

import serial
import matplotlib.pyplot as plt
import time

port = '/dev/ttyUSB0'
baudrate = 115200
ser = serial.Serial(port, baudrate)

# Setup the plot
plt.ion()
fig, ax = plt.subplots()
xs = []
ys = []

# Set a flag to stop the loop after 50 milliseconds
stop_flag = False
start_time = time.time()
stop_time = start_time + 0.05  # 50 milliseconds

while not stop_flag:
    # Read a line of data from the serial port
    data = ser.readline().decode().rstrip()

    # Convert the line of data to a number
    try:
        y = float(data)
    except ValueError:
        continue

    xs.append(len(xs))
    ys.append(y)

    ax.clear()
    ax.plot(xs, ys)
    plt.draw()
    plt.pause(0.001)

    # Check if the stop time has been reached
    if time.time() >= stop_time:
        stop_flag = True

# Close the serial connection and plot
ser.close()
plt.show()
