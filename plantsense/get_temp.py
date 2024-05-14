import Adafruit_DHT
from datetime import datetime
import time 

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def log_temperature_humidity_once(file_path="temp.txt"):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        message = f"Temp={temperature:.0f}C Humidity={humidity:.2f}% "
        print(message)
        with open(file_path,"a") as file:
            file.write(message + datetime.now().strftime("%Y/%m/%d %H:%M")+"\n")
    else:
        print("Failed to retrieve data from sensor, check wiring")


def log_temperature_humidity_interval(interval, file_path="temp.txt"):

    while True:
        log_temperature_humidity_once()
        time.sleep(interval)
    
def log_temperature_humidity_for_seconds(seconds, file_path="temp.txt"):
    end_time = time.time() + seconds
    while time.time() < end_time:
        log_temperature_humidity_once()
        time.sleep(1)
    print("Exiting Program...")

if __name__ == "__main__":
    file_path = "temp.txt"
    log_temperature_humidity_for_seconds(10, file_path)
