#!/bin/python3

import serial
import matplotlib.pyplot as plt

port = '/dev/ttyUSB0'
baudrate = 115200
ser = serial.Serial(port, baudrate)

# Setup the plot
plt.ion()
fig, ax = plt.subplots()
xs = []
ys = []

while True:
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
