"""Summary

Code plots accelerometer data

Attributes:
    acc_x_array (list): Description
    acc_x_plot (TYPE): Description
    acc_y_array (list): Description
    acc_y_plot (TYPE): Description
    acc_z_array (list): Description
    acc_z_plot (TYPE): Description
    animate_plot (TYPE): Description
    fig (TYPE): Description
    ser (TYPE): Description
    time_stamps_acc (list): Description
    time_start (TYPE): Description
"""
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

import random

# For Linux systems

# ser = serial.Serial('/dev/ttyUSB0')

# For Windows

ser = serial.Serial('COM10')

ser.baudrate = 115200

acc_x_array = []
acc_y_array = []
acc_z_array = []

fig = plt.figure()
fig.suptitle('Accelerometer x y z data vs time', fontsize=12)

# Enter in a row, column, idx format

# 3 X 1 plots, Plot 1
acc_x_plot = fig.add_subplot(3, 1, 1)
# 3 X 1 plots, Plot 2
acc_y_plot = fig.add_subplot(3, 1, 2)
# 3 X 1 plots, Plot 3
acc_z_plot = fig.add_subplot(3, 1, 3)

time_stamps_acc = []

time_start = time.time()


# while ser.isOpen():


def AnimatePlots(i):
    """Function to animate the plots

    Args:
        i (TYPE): Description

    """

    global time_start

    global acc_x_array
    global acc_y_array
    global acc_z_array

    global acc_x_plot
    global acc_y_plot
    global acc_z_plot

    # Convert from ascii encoding

    decoded_raw_data = ser.readline().decode("ascii")

    # Get the data code for acc, gyr and mag

    data_code = decoded_raw_data[0:3]

    if data_code == 'acc':
        acc_data = decoded_raw_data[3:]

        acc_data_list = acc_data.split(',')

        acc_x_array.append(float(acc_data_list[0]))
        acc_y_array.append(float(acc_data_list[1]))
        acc_z_array.append(float(acc_data_list[2]))

        time_stamps_acc.append(time.time() - time_start)

        acc_x_plot.plot(time_stamps_acc, acc_x_array, 'r')
        acc_y_plot.plot(time_stamps_acc, acc_y_array, 'r')
        acc_z_plot.plot(time_stamps_acc, acc_z_array, 'r')


animate_plot = animation.FuncAnimation(fig, AnimatePlots, interval=10)
plt.show()
