import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

import random

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate=115200

acc_data_x = [0]
acc_data_y = [0]
acc_data_z = [0]
gyr_data_x = [0]
gyr_data_y = [0]
gyr_data_z = [0]
mag_data_x = [0]
mag_data_y = [0]
mag_data_z = [0]


fig = plt.figure()

# 3 X 3 plots, Plot 1
acc_x_plot = fig.add_subplot(3,3,1)
# 3 X 3 plots, Plot 2
acc_y_plot = fig.add_subplot(3,3,2)
# 3 X 3 plots, Plot 3
acc_z_plot = fig.add_subplot(3,3,3)

# 3 X 3 plots, Plot 4
gyr_x_plot = fig.add_subplot(3,3,4)
# 3 X 3 plots, Plot 5
gyr_y_plot = fig.add_subplot(3,3,5)
# 3 X 3 plots, Plot 6
gyr_z_plot = fig.add_subplot(3,3,6)

# 3 X 3 plots, Plot 7
mag_x_plot = fig.add_subplot(3,3,7)
# 3 X 3 plots, Plot 8
mag_y_plot = fig.add_subplot(3,3,8)
# 3 X 3 plots, Plot 9
mag_z_plot = fig.add_subplot(3,3,9)


count = 1

times_coord = []
time_s = time.time()

# while ser.isOpen():
def AnimatePlots(i):
	global time_s

	global acc_data_x
	global acc_data_y
	global acc_data_z

	global gyr_data_x
	global gyr_data_y
	global gyr_data_z

	global mag_data_x
	global mag_data_y
	global mag_data_z

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

	imu_data = ser.readline().decode("ascii")

	# Update the time coordinate

	times_coord.append(time.time()-time_s)

	# Get the data code for acc, gyr and mag

	data_code = imu_data[0:3]

	if data_code == 'acc':


		acc_data = imu_data[3:]

		acc_data_list =acc_data.split(',')

		acc_data_x.append(float(acc_data_list[0]))
		acc_data_y.append(float(acc_data_list[1]))
		acc_data_z.append(float(acc_data_list[2]))
	
	if data_code == 'gyr':


		gyr_data = imu_data[3:]

		gyr_data_list =gyr_data.split(',')

		gyr_data_x.append(float(gyr_data_list[0]))
		gyr_data_y.append(float(gyr_data_list[1]))
		gyr_data_z.append(float(gyr_data_list[2]))
	
	if data_code == 'mag':

		mag_data = imu_data[3:]

		mag_data_list =mag_data.split(',')

		mag_data_x.append(float(mag_data_list[0]))
		mag_data_y.append(float(mag_data_list[1]))
		mag_data_z.append(float(mag_data_list[2]))

	try:

		acc_x_plot.plot(times_coord, acc_data_x, 'r')

	except ValueError:
		acc_data_x.append(0)
		acc_x_plot.plot(times_coord, acc_data_x, 'r')

	try:
		acc_y_plot.plot(times_coord, acc_data_y, 'r')
	except ValueError:
		acc_data_y.append(0)
		acc_y_plot.plot(times_coord, acc_data_y, 'r')
	
	try:
		acc_z_plot.plot(times_coord, acc_data_z, 'r')
	except ValueError:
		acc_data_z.append(0)
		acc_z_plot.plot(times_coord, acc_data_z, 'r')
	
	try:
		gyr_x_plot.plot(times_coord, gyr_data_x, 'b')
	except ValueError:
		gyr_data_x.append(0)
		gyr_x_plot.plot(times_coord, gyr_data_x, 'b')
	
	try:
		gyr_y_plot.plot(times_coord, gyr_data_y, 'b')
	except ValueError:
		gyr_data_y.append(0)
		gyr_y_plot.plot(times_coord, gyr_data_y, 'b')
	
	try:
		gyr_z_plot.plot(times_coord, gyr_data_z, 'b')
	except ValueError:
		gyr_data_z.append(0)
		gyr_z_plot.plot(times_coord, gyr_data_z, 'b')
	
	try:
		mag_x_plot.plot(times_coord, mag_data_x, 'g')
	except ValueError:
		mag_data_x.append(0)
		mag_x_plot.plot(times_coord, mag_data_x, 'g')

	try:
		mag_y_plot.plot(times_coord, mag_data_y, 'g')
	except ValueError:
		mag_data_y.append(0)
		mag_y_plot.plot(times_coord, mag_data_y, 'g')

	try:
		mag_z_plot.plot(times_coord, mag_data_z, 'g')
	except ValueError:
		mag_data_z.append(0)
		mag_z_plot.plot(times_coord, mag_data_z, 'g')


ani = animation.FuncAnimation(fig, AnimatePlots, interval=10)
plt.show()