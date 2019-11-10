void setup() {
  Serial.begin(115200);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(15, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
  pinMode(16, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
}

void loop() {
  if (!digitalRead(2)) {
    Serial.print("C2");
    while (!digitalRead(2)) {
      delay(30);
    }
  }
  if (!digitalRead(3)) {
    Serial.print("C1");
    while (!digitalRead(3)) {
      delay(30);
    }
  }
  if (!digitalRead(4)) {
    Serial.print("T2");
    while (!digitalRead(4)) {
      delay(30);
    }
  }
  if (!digitalRead(5)) {
    Serial.print("T1");
    while (!digitalRead(5)) {
      delay(30);
    }
  }
  if (!digitalRead(6)) {
    Serial.print("C5");
    while (!digitalRead(6)) {
      delay(30);
    }
  }
  if (!digitalRead(15)) {
    Serial.print("T1");
    while (!digitalRead(15)) {
      delay(30);
    }
  }
  if (!digitalRead(14)) {
    Serial.println("T2");
    while (!digitalRead(14)) {
      delay(30);
    }
  }
  if (!digitalRead(16)) {
    Serial.print("T3");
    while (!digitalRead(16)) {
      delay(30);
    }
  }
  if (!digitalRead(10)) {
    Serial.print("T4");
    while (!digitalRead(10)) {
      delay(30);
    }
  }
}
