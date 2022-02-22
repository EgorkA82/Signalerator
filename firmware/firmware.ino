#define OUTPUT_PIN A0

int val = 0;

void setup() {
  Serial.begin(9600);
  pinMode(OUTPUT_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
      val = Serial.readStringUntil('\n').toInt();
      if (val > 255) val = 255;
      if (val < 0) val = 0;

      Serial.println(val);
      analogWrite(OUTPUT_PIN, val);
  }
}