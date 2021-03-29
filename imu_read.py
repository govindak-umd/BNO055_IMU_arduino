"""Code to read IMU Data through pyserial

Attributes:
    ser (TYPE): Serial
"""
import serial
# For Linux systems

# ser = serial.Serial('/dev/ttyUSB0')

# For Windows

ser = serial.Serial('COM10')

ser.baudrate = 115200

while ser.isOpen():

    # Convert from ascii encoding

    imu_data = ser.readline().decode("ascii")

    data_code = imu_data[0:3]

    if data_code == 'acc':
        acc_data = imu_data[3:]

        acc_data_list = acc_data.split(',')

        print(acc_data_list)

    if data_code == 'gyr':
        gyr_data = imu_data[3:]

        gyr_data_list = gyr_data.split(',')
        print(gyr_data_list)

    if data_code == 'mag':
        mag_data = imu_data[3:]

        mag_data_list = mag_data.split(',')
        print(mag_data_list)
