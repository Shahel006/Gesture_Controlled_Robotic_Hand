#include <Servo.h>

Servo thumb, indexF, middle, ring, pinky;

String input = "";

void setup() {
  Serial.begin(9600);

  // Attach servos to pins
  thumb.attach(5);
  indexF.attach(3);
  middle.attach(6);
  ring.attach(9);
  pinky.attach(10);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      processData(input);
      input = "";
    } else {
      input += c;
    }
  }
}

// -----------------------------
// PROCESS DATA FROM PYTHON
// -----------------------------
void processData(String data) {
  int t, i, m, r, p;

  sscanf(data.c_str(), "%d,%d,%d,%d,%d", &t, &i, &m, &r, &p);

  thumb.write(t);
  indexF.write(i);
  middle.write(m);
  ring.write(r);
  pinky.write(p);
}