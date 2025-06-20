import serial
import mysql.connector
from datetime import datetime

# Replace with your actual COM port for ESP8266 (check Device Manager)
ser = serial.Serial('COM3', 115200)  # Change 'COM5' to your ESP8266's port

# Connect to MySQL database (XAMPP or other)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",           # Default XAMPP password is empty
    database="nodetemp" # Make sure this database exists
)

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS temperature_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

print("Listening for temperature data from ESP8266...")

while True:
    try:
        line = ser.readline().decode(errors='ignore').strip()

        if line:
            try:
                temperature = float(line)
                print(temperature)

                cursor.execute("INSERT INTO temperature_data (temperature) VALUES (%s)", (temperature,))
                conn.commit()
            except ValueError:
                print(f"Ignored non-temp data: {line}")

    except Exception as e:
        print("Error:", e)
        break

ser.close()
conn.close()
