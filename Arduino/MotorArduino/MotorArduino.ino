const int JOYSTICK_PIN = A2;
const uint8_t INSTRUCTION_GOAL_POSITION = 0x1E;

void setup() {
    Serial.begin(19200);
}

void loop() {
    int sensorValue = analogRead(JOYSTICK_PIN);
    uint16_t targetPosition = (uint16_t)map(sensorValue, 0, 1023, 818, 511);

    Serial.write(INSTRUCTION_GOAL_POSITION);
    Serial.write((uint8_t*)&targetPosition, sizeof(targetPosition));

    delay(100);
}
