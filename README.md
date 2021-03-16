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

Graphs available

- 9 Axis data - *plot_all_9axis_live.py*
<p align="center">
  <img height="500" src="Images/9_imu.png">
</p>

- Accelerometer 3-axis data - *plot_acc.py*
<p align="center">
  <img height="500" src="Images/3_acc.png">
</p>



Code explanations:

| Serial Number| Code  | Function |
| ------------- | ------------- | ------------- |
| 1  | imu_test.ino | To access Acceleratometer, Gyroscope and Magnetometer data  |
| 2 |  imu_read.py| Code to access the serial imu data and display the results |
| 3  |  plot_all_9axis_live.py | Access all 9 axis Serial data through python scripts |
| 4 | plot_acc.py | Plotting only acceleratometer data|
| 5 | | |
 
