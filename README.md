 🌡️🔥 IoT-Based Temperature & Gas Monitoring System Using NodeMCU (ESP8266)

🔍 Overview

This project builds a smart IoT-based environmental monitoring system using the **NodeMCU ESP8266 Wi-Fi microcontroller**. It uses a **temperature sensor** (like DHT11 or DS18B20) and a **gas sensor** (like MQ-2 or MQ-135) to sense ambient conditions and send data wirelessly to a **Python Flask server**. The server stores the data in a **MySQL database** hosted using **XAMPP**. This is useful for indoor air quality monitoring, industrial safety, or smart home applications.



🛠️ Features

* 📶 Wireless sensor data transmission via Wi-Fi
* 🌡️ Temperature monitoring
* 💨 Gas detection (smoke, CO₂, LPG, etc.)
* 🐍 Python-based local server
* 💾 MySQL database logging via XAMPP
* 📈 Extendable to cloud platforms or dashboards



⚙️ Hardware Components

* 📡 **NodeMCU (ESP8266)**
* 🌡️ **DHT11** or **DS18B20** (Temperature Sensor)
* 💨 **MQ-2** or **MQ-135** (Gas Sensor)
* 🔧 Jumper wires and Breadboard
* 🔋 USB Cable for power

---

💻 Software Stack

| Tool        | Purpose                              |
| ----------- | ------------------------------------ |
| Arduino IDE | Flashing code to NodeMCU             |
| Python 3.x  | Flask server to handle sensor data   |
| XAMPP       | Local MySQL + Apache server          |
| HeidiSQL    | GUI for MySQL database visualization |



🔧 How It Works

1. **Sensors + NodeMCU:**

   * NodeMCU reads data from the temperature sensor and gas sensor.
   * It sends this data to a Flask server running on a local PC via HTTP POST.

2. **Python Flask Server:**

   * The server receives the temperature and gas values.
   * It stores the readings in a MySQL database.

3. **Database Layer:**

   * The MySQL database is hosted locally via XAMPP.
   * You can monitor data using phpMyAdmin or HeidiSQL.


🚀 Getting Started

### 1. 🛠 Hardware Connections

#### 🧪 Sensor Pinouts

* **DHT11 / DS18B20:**

  ```
  VCC  -> 3.3V
  GND  -> GND
  DATA -> D2 (GPIO4)
  Pull-up resistor (10kΩ) between DATA & VCC
  ```

* **MQ-2 / MQ-135 (Analog Out):**

  ```
  VCC  -> 3.3V
  GND  -> GND
  AOUT -> A0 (Analog Pin)
  ```

---

2. 💡 Arduino IDE Setup

* Install **ESP8266 board package** from Board Manager

* Install required libraries:

  * `DHT.h` (for DHT11) or `OneWire.h` & `DallasTemperature.h` (for DS18B20)
  * `ESP8266WiFi.h`
  * `ESP8266HTTPClient.h`

* Flash the code in `/NodeMCU_Code/main.ino`

  * Configure:

    * Wi-Fi SSID and password
    * Server IP (your PC IP)
    * Temperature sensor type (DHT11 or DS18B20)

---

3. 🐍 Python Flask Server Setup

* Required packages:

```bash
pip install flask mysql-connector-python
```

* Run the script `/Server_Code/server.py`:

```bash
python server.py
```

* Flask listens on your local IP (e.g., `http://192.168.1.10:5000/postdata`)


4. 🗃️ MySQL Database Setup with XAMPP

* Start **Apache** and **MySQL** from XAMPP Control Panel
* Use **phpMyAdmin** or **HeidiSQL** to create:

📂 Database: `env_monitoring`

📄 Table:

```sql
CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT NOT NULL,
    gas_level INT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```



 📊 Sample Output Table

| ID | Temperature | Gas Level | Timestamp           |
| -- | ----------- | --------- | ------------------- |
| 1  | 28.3        | 180       | 2025-06-20 11:05:00 |
| 2  | 29.1        | 220       | 2025-06-20 11:10:10 |


📸 Optional Visuals

* 📷 ESP8266 Circuit Setup
* 🧠 Sensor output on Serial Monitor
* 📊 Screenshot of MySQL table
* 🧾 Real-time Flask data logs



 🚀 Future Enhancements

* Add humidity (from DHT11) to database
* Visualize data using HTML/CSS dashboard
* Add SMS/Email alerts for high gas levels
* Send data to cloud (e.g., Firebase or ThingSpeak)
* Control a fan or buzzer based on thresholds






