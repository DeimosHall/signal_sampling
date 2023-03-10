#define SIGNAL 34

enum DelayTime {
  t20Hz = 50000,
  t50Hz = 20000,
  t100Hz = 10000,
  t1kHz =  1000,
  t10kHz = 100,
};

unsigned long samplingTime = t10kHz;
int bits[8] = {2, 4, 5, 18, 19, 21, 22, 23};

void setup() {
  Serial.begin(115200);
  pinMode(SIGNAL, INPUT);
  for(int i = 0; i < 8; i++) {
    pinMode(bits[i], OUTPUT);
  }
  // Serial.println("Sampling time: " + String(samplingTime));
  // delay(3000);
}

void loop() {
  int adcValue = analogRead(SIGNAL);

  int bitsVal = map(adcValue, 0, 4095, 0, 255);
  Serial.println(bitsVal);
  for(int i = 0; i < 8; i++) {
    if(bitsVal & (1 << i)) {
      digitalWrite(bits[i], HIGH);
    } else {
      digitalWrite(bits[i], LOW);
    }
  }

  delayMicroseconds(samplingTime);
}
