"""Summary Code tp read and plot data, live.

Attributes:
    acc_x_array (list): Description
    acc_x_plot (TYPE): Description
    acc_y_array (list): Description
    acc_y_plot (TYPE): Description
    acc_z_array (list): Description
    acc_z_plot (TYPE): Description
    ani (TYPE): Description
    fig (TYPE): Description
    gyr_x_array (list): Description
    gyr_x_plot (TYPE): Description
    gyr_y_array (list): Description
    gyr_y_plot (TYPE): Description
    gyr_z_array (list): Description
    gyr_z_plot (TYPE): Description
    mag_x_array (list): Description
    mag_x_plot (TYPE): Description
    mag_y_array (list): Description
    mag_y_plot (TYPE): Description
    mag_z_array (list): Description
    mag_z_plot (TYPE): Description
    ser (TYPE): Description
    time_start (TYPE): Description
    time_stamps (list): Description
"""
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

import random

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate=115200

acc_x_array = []
acc_y_array = []
acc_z_array = []
gyr_x_array = []
gyr_y_array = []
gyr_z_array = []
mag_x_array = []
mag_y_array = []
mag_z_array = []


fig = plt.figure()
fig.suptitle('Accelerometer x y z data vs time', fontsize=12)

# Enter in a row, column, idx format

# 3 X 3 plots, Plot 1
acc_x_plot = fig.add_subplot(3,1,1)
# 3 X 3 plots, Plot 2
acc_y_plot = fig.add_subplot(3,1,2)
# 3 X 3 plots, Plot 3
acc_z_plot = fig.add_subplot(3,1,3)

# # 3 X 3 plots, Plot 4
# gyr_x_plot = fig.add_subplot(3,3,4)
# # 3 X 3 plots, Plot 5
# gyr_y_plot = fig.add_subplot(3,3,5)
# # 3 X 3 plots, Plot 6
# gyr_z_plot = fig.add_subplot(3,3,6)

# # 3 X 3 plots, Plot 7
# mag_x_plot = fig.add_subplot(3,3,7)
# # 3 X 3 plots, Plot 8
# mag_y_plot = fig.add_subplot(3,3,8)
# # 3 X 3 plots, Plot 9
# mag_z_plot = fig.add_subplot(3,3,9)


time_stamps_acc = []
time_stamps_gyr = []
time_stamps_mag = []

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

	global gyr_x_array
	global gyr_y_array
	global gyr_z_array

	global mag_x_array
	global mag_y_array
	global mag_z_array

	global acc_x_plot
	global acc_y_plot
	global acc_z_plot

	global gyr_x_plot
	global gyr_y_plot
	global gyr_z_plot

	global mag_x_plot
	global mag_y_plot
	global mag_z_plot

	# Convert from ascii encoding

	decoded_raw_data = ser.readline().decode("ascii")

	# Get the data code for acc, gyr and mag

	data_code = decoded_raw_data[0:3]

	if data_code == 'acc':


		acc_data = decoded_raw_data[3:]

		acc_data_list =acc_data.split(',')

		acc_x_array.append(float(acc_data_list[0]))
		acc_y_array.append(float(acc_data_list[1]))
		acc_z_array.append(float(acc_data_list[2]))
	
		time_stamps_acc.append(time.time()-time_start)

		acc_x_plot.plot(time_stamps_acc, acc_x_array, 'r')
		acc_y_plot.plot(time_stamps_acc, acc_y_array, 'r')
		acc_z_plot.plot(time_stamps_acc, acc_z_array, 'r')

	# if data_code == 'gyr':


	# 	gyr_data = decoded_raw_data[3:]

	# 	gyr_data_list =gyr_data.split(',')

	# 	gyr_x_array.append(float(gyr_data_list[0]))
	# 	gyr_y_array.append(float(gyr_data_list[1]))
	# 	gyr_z_array.append(float(gyr_data_list[2]))

	# 	time_stamps_gyr.append(time.time()-time_start)

	# 	gyr_x_plot.plot(time_stamps_gyr, gyr_x_array, 'b')
	# 	gyr_y_plot.plot(time_stamps_gyr, gyr_y_array, 'b')
	# 	gyr_z_plot.plot(time_stamps_gyr, gyr_z_array, 'b')
	
	# if data_code == 'mag':

	# 	mag_data = decoded_raw_data[3:]

	# 	mag_data_list =mag_data.split(',')

	# 	mag_x_array.append(float(mag_data_list[0]))
	# 	mag_y_array.append(float(mag_data_list[1]))
	# 	mag_z_array.append(float(mag_data_list[2]))

	# 	time_stamps_mag.append(time.time()-time_start)

	# 	mag_x_plot.plot(time_stamps_mag, mag_x_array, 'g')
	# 	mag_y_plot.plot(time_stamps_mag, mag_y_array, 'g')
	# 	mag_z_plot.plot(time_stamps_mag, mag_z_array, 'g')

ani = animation.FuncAnimation(fig, AnimatePlots, interval=10)
plt.show()