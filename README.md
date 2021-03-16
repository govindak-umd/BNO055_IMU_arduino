# BNO055_IMU_arduino

This repo shows you how to use BNO055 IMU

Hardware needed:

- BNO055 9-axis IMU sensor 
- Arduino (Nano used here)
- Male to Male Jumpers
- Breadboard
- Arduino to PC USB Cable

Wiring should be done as shown in the image below:

<p align="center">
  <img height="500" src="Images/setup.jpeg">
</p>

The connections are laid out here:

| Connect From Arduino |  Connect To IMU |
| ------------- | ------------- | 
| A4  | SDA  | 
| A5 | SCL | 
| GND | GND  | 
| 5V | Vin | 

Install the following on your Arduino IDE by going to **Tools > Manage Libraries**

- Arduino BNO055
- Adafruit Unified Sensor

Install Pyserial

    pip install pyserial

Verify the USB Port by entering:

    ls /dev/tty

After verifying, make this port an executable by entering:

    sudo chmod a+rw /dev/ttyUSB0 

Code explanations:

| Serial Number| Code  | Function |
| ------------- | ------------- | ------------- |
| 1  | imu_test.ino | To access Acceleratometer, Gyroscope and Magnetometer data  |
| 2 |  imu_read.py| Code to access the serial imu data and display the results |
| 3  |  py_serial_test.py | Access Serial data through python scripts |
| 4 |  | |
| 5 | | |
 
