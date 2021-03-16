#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 myIMU = Adafruit_BNO055(55);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  myIMU.begin();
  delay(1000);
  int8_t temp= myIMU.getTemp();
  myIMU.setExtCrystalUse(true);
  Serial.println(temp);
}

void loop() {

  uint8_t system, acc, gyro, mag = 0;
  
  // To get the system callibrations good, you must get the acc, gyro and mag callibration good
  // Make sure all the values come upto 3, for fullc callibration
  // Gyro is the most easy to callibrate (30 seconds - 1 min)
  // Magnetometer callibration - Swing around in figure around 8 (30 seconds - 1 min)
  // Accelerometer - Move and hold in all axes for full callibration (30 seconds - 1 min)
  
  myIMU.getCalibration(&system, &gyro, &acc, &mag);
  Serial.print("Callibration Data : ");
  Serial.print(acc);
  Serial.print(" , ");
  Serial.print(gyro);
  Serial.print(" , ");
  Serial.print(mag);
  Serial.print(" , ");
  Serial.println(system);

  imu::Vector<3> acc_vec = myIMU.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  Serial.print("Accelerometer Values : ");
  Serial.print(acc_vec.x());
  Serial.print(",");
  Serial.print(acc_vec.y());
  Serial.print(",");
  // Verify the callibration by making sure the acc_vec.z() is around 9.8 m/s^2
  Serial.println(acc_vec.z());
  delay(BNO055_SAMPLERATE_DELAY_MS);
}
