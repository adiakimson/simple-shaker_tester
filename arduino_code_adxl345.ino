#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

// Create an instance of the sensor
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

void setup() {
  Serial.begin(9600);

  // Initialize the sensor
  if (!accel.begin()) {
    Serial.println("Ooops, no ADXL345 detected ... Check your wiring!");
    while (1);
  }

  // Set range to +/- 2G (can also be set to 4G, 8G, or 16G)
  accel.setRange(ADXL345_RANGE_2_G);
}

void loop() {
  // Get the accelerometer data
  sensors_event_t event;
  accel.getEvent(&event);

  // Print the data
  Serial.print("X: ");
  Serial.print(event.acceleration.x);
  Serial.print(" \tY: ");
  Serial.print(event.acceleration.y);
  Serial.print(" \tZ: ");
  Serial.println(event.acceleration.z);

  // Delay before next read
  delay(500);
}
