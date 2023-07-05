
#include <Servo.h>
#include "BraccioRobot.h"
#define INPUT_BUFFER_SIZE 64

static char inputBuffer[INPUT_BUFFER_SIZE];
Position armPosition;

void setup() {
  Serial.begin(115200);
  BraccioRobot.init();
}

void loop() {
    handleSerialInput();    
}

void handleSerialInput() {
  if (!Serial.available()) return;
  byte byte_count = Serial.readBytesUntil('\n', inputBuffer, INPUT_BUFFER_SIZE);
  inputBuffer[byte_count] = '\0';
  interpretCommand(inputBuffer, byte_count);
}

void interpretCommand(char* inputBuffer, byte commandLength) {
  if (inputBuffer[0] == 'P') {
    positionArm(inputBuffer + 1);
  } else if (inputBuffer[0] == 'H') {
    homePositionArm();
  } else if (inputBuffer[0] == '0') {
    BraccioRobot.powerOff();
    Serial.println("OK");
  }  else if (inputBuffer[0] == '1') {
    BraccioRobot.powerOn();
    Serial.println("OK");
  } else {
    Serial.println("E0");
  }
  Serial.flush();
}

void
positionArm(char *in) {
  int speed = armPosition.setFromString(in);
  if (speed > 0) {
    BraccioRobot.moveToPosition(armPosition, speed);
    Serial.println("OK");
  } else {
    Serial.println("E1");
  }
}

void
homePositionArm() {
  BraccioRobot.moveToPosition(armPosition.set(90, 90, 90, 90, 90, 73), 150);
  Serial.println("OK");
}
