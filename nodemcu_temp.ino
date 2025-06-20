#define TEMP_PIN A0  // A0 is the only analog input on ESP8266

void setup() {
  Serial.begin(115200);
}

void loop() {
  int analogValue = analogRead(TEMP_PIN);  // Read analog value (0-1023)

  // Convert analog value to voltage (ESP8266 A0 range is 0-1V by default)
  float voltage = analogValue * (3.3 / 1023.0);  // if using bare A0 (0–1V input range)

  // If you're using a voltage divider to scale 3.3V to 1V, change formula:
  // float voltage = analogValue * (3.3 / 1023.0);

  // Assuming LM35-like sensor: 10mV per °C
  float temperatureC = voltage * 1000 / 10;

  
  Serial.print(temperatureC);
  Serial.println("\n");
 

  delay(1000);
}
