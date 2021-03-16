#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_DELAY_MS (1000)

Adafruit_BNO055 myIMU = Adafruit_BNO055();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  myIMU.begin();
  delay(1000);
  int8_t temp= myIMU.getTemp();
  Serial.println(temp);
}

void loop() {

  imu::Vector<3> acc_vec = myIMU.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> gyro_vec = myIMU.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  imu::Vector<3> mag_vec = myIMU.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER);

  Serial.print("acc");
  Serial.print(acc_vec.x());
  Serial.print(",");
  Serial.print(acc_vec.y());
  Serial.print(",");
  Serial.println(acc_vec.z());

  Serial.print("gyr");
  Serial.print(gyro_vec.x());
  Serial.print(",");
  Serial.print(gyro_vec.y());
  Serial.print(",");
  Serial.println(gyro_vec.z());

  Serial.print("mag");
  Serial.print(mag_vec.x());
  Serial.print(",");
  Serial.print(mag_vec.y());
  Serial.print(",");
  Serial.println(mag_vec.z());
  
  delay(BNO055_SAMPLERATE_DELAY_MS);
}
