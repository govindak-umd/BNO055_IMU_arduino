"""Code to convert quarternion data to euler angles

Attributes:
    ser (TYPE): Serial
"""
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import math

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 115200

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

def euler_from_quaternion(quarternion_list):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """

        x = float(quarternion_list[0])
        y = float(quarternion_list[1])
        z = float(quarternion_list[2])
        w = float(quarternion_list[3])

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        # data returned in radians
        return roll_x, pitch_y, yaw_z

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

    calc_roll, calc_pitch, calc_yaw = euler_from_quaternion(imu_data_list)
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

    if len(time_stamps_rpy_plot)>15:

        roll_array.pop(0)
        pitch_array.pop(0)
        yaw_array.pop(0)
        time_stamps_rpy_plot.pop(0)

try:

    animate_plot = animation.FuncAnimation(fig, AnimateRPYPlots, interval=1)
    plt.show()

# Save when the user exits

except KeyboardInterrupt:

    print('File closed and saved upon user request')