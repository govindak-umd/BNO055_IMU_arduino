"""Code to save quaternion data to a txt file

Attributes:
    ser (TYPE): Serial
"""
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import math

# For Linux systems

# ser = serial.Serial('/dev/ttyUSB0')

# For Windows

ser = serial.Serial('COM10')

ser.baudrate = 9600

fig = plt.figure()
fig.suptitle('Roll, Pitch, Yaw data vs time', fontsize=12)

# Enter in a row, column, idx format

# 3 X 1 plots, Plot 1
roll_plot = fig.add_subplot(3, 1, 1)
# 3 X 1 plots, Plot 2
pitch_plot = fig.add_subplot(3, 1, 2)
# 3 X 1 plots, Plot 3
yaw_plot = fig.add_subplot(3, 1, 3)

time_stamps_rpy = []

time_start = time.time()

f = open("quaternion_data.txt", "w+")


def euler_from_quaternion(quaternion_list):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """

    x = float(quaternion_list[0])
    y = float(quaternion_list[1])
    z = float(quaternion_list[2])
    w = float(quaternion_list[3])

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    yaw_z = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    roll_x = math.atan2(t3, t4)

    # data returned in radians
    # return roll_x, pitch_y, yaw_z

    # returning data in degrees
    yaw_z = yaw_z * (180 / math.pi)
    pitch_y = pitch_y * (180 / math.pi)
    roll_x = roll_x * (180 / math.pi)
    return yaw_z, pitch_y, roll_x


# To keep a record
quart_array = []

# To plot

roll_array = []
pitch_array = []
yaw_array = []


def AnimateRPYPlots(i):
    # To make sure the x axis is kept in check

    time_stamps_rpy_plot = time_stamps_rpy

    # Convert from ascii encoding

    imu_data = ser.readline().decode("ascii")

    # Split at the tab

    imu_data_list = imu_data.split('\t')

    # Remove off the '\r\n' at the end of the line

    imu_data_list.pop()

    # Keep a record of all the quarts recorded

    quart_array.append(imu_data_list)

    # Show in the terminal
    print('Quaternion data : ', imu_data_list)
    f.write(str(time.strftime('%H:%M:%S')) + ' ' + str(imu_data_list[0]) + ' ' + str(imu_data_list[1]) + ' ' + str(imu_data_list[2]) + ' ' + str(
        imu_data_list[3]) + "\n")

    calc_yaw, calc_pitch, calc_roll = euler_from_quaternion(imu_data_list)
    roll_array.append(calc_roll)
    pitch_array.append(calc_pitch)
    yaw_array.append(calc_yaw)
    # Save the time stamp

    time_stamps_rpy_plot.append(time.time() - time_start)

    # Save for plotting purposes

    roll_plot.plot(time_stamps_rpy_plot, roll_array, 'r')
    pitch_plot.plot(time_stamps_rpy_plot, pitch_array, 'g')
    yaw_plot.plot(time_stamps_rpy_plot, yaw_array, 'b')

    # Removing old points off so that the
    # graph is not very cluttered

    if len(time_stamps_rpy_plot) > 15:
        roll_array.pop(0)
        pitch_array.pop(0)
        yaw_array.pop(0)
        time_stamps_rpy_plot.pop(0)

try:

    animate_plot = animation.FuncAnimation(fig, AnimateRPYPlots, interval=5)
    plt.show()

# Save when the user exits
except KeyboardInterrupt:
    print('File closed and saved upon user request')
    f.close()
