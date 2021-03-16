import serial
from matplotlib import pyplot as plt

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate=115200

acc_data_x = []
acc_data_y = []
acc_data_z = []
gyr_data_x = []
gyr_data_y = []
gyr_data_z = []
mag_data_x = []
mag_data_y = []
mag_data_z = []

def PlotData():

	global acc_data_x
	global acc_data_y
	global acc_data_z
	global gyr_data_x
	global gyr_data_y
	global gyr_data_z
	global mag_data_x
	global mag_data_y
	global mag_data_z
	pass

while ser.isOpen():

	# Convert from ascii encoding

	imu_data = ser.readline().decode("ascii")

	# Read the Line header
	
	data_code = imu_data[0:3]
	if data_code == 'acc':
		print('Acceleratometer data > ')
		print(imu_data[3:])
	if data_code == 'gyr':
		print('Gyroscope data > ')
		print(imu_data[3:])
	if data_code == 'mag':
		print('Magnetometer data > ')
		print(imu_data[3:])