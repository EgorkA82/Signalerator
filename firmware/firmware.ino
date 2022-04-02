#define OUTPUT_PIN 3

byte val = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if (Serial.available()) {
      val = Serial.parseInt();
      analogWrite(OUTPUT_PIN, val);
  }
}