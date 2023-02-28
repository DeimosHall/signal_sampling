#define SIGNAL 15

int frequency = 20;
unsigned long lastTime = 0, samplingTime = 1 / frequency;

void setup() {
  pinMode(SIGNAL, INPUT);
  Serial.begin(115200);
}

void loop() {
  if (millis() - lastTime >= samplingTime) {
    lastTime = millis();
    int adcValue = analogRead(SIGNAL);
    float voltage = adcValue * 3.3 / 4095;
    Serial.println(voltage);
  }
}