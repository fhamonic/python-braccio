#include <Servo.h>
#include "BraccioRobot.h"
#define INPUT_BUFFER_SIZE 64

static char inputBuffer[INPUT_BUFFER_SIZE];
Position armPosition;

void setup() {
    Serial.begin(115200);
    BraccioRobot.init(armPosition.set(0, 30, 0, 0, 90, 73));
}

void loop() { handleSerialInput(); }

void handleSerialInput() {
    if(!Serial.available()) return;
    size_t byte_count =
        Serial.readBytesUntil('\n', inputBuffer, INPUT_BUFFER_SIZE);
    inputBuffer[byte_count] = '\0';
    interpretCommand(inputBuffer, byte_count);
}

void interpretCommand(char * inputBuffer, byte commandLength) {
    if(inputBuffer[0] == 'P') {
        positionArm(inputBuffer + 1);
    } else if(inputBuffer[0] == '0') {
        BraccioRobot.powerOff();
        Serial.println("OK");
    } else if(inputBuffer[0] == '1') {
        BraccioRobot.powerOn();
        Serial.println("OK");
    } else {
        Serial.print("Unknown command: '");
        Serial.print(inputBuffer);
        Serial.println("'");
    }
    Serial.flush();
}

void positionArm(char * in) {
    int speed = armPosition.setFromString(in);
    if(speed < 0) {
        Serial.println("Invalid position: '");
        Serial.print(inputBuffer);
        Serial.println("'");
        return;
    }
    BraccioRobot.moveToPosition(armPosition, speed);
    Serial.println("OK");
}
