int ledRed = 2;

void setup() {
  Serial.begin(9600);
  pinMode(ledRed, OUTPUT);
  digitalWrite(ledRed, HIGH);
}

void loop() {
  int lightValue = analogRead(A0);
  Serial.println(lightValue);

  if (lightValue < 200)
  {
    digitalWrite(ledRed, HIGH);
  }

  else
  {
    digitalWrite(ledRed, LOW);
  }

  delay(1000);
}