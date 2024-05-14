import time 
import Adafruit_ADS1x15
from datetime import datetime

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

# THRESHOLDS for soil moisture
DRY_THRESHOLD = 16000
WET_THRESHOLD = 9000


def capture_moisture_once(file_path="soil_moisture.txt"):
    raw_value = adc.read_adc(3, gain=GAIN)
    if raw_value > DRY_THRESHOLD:
        moisture_level = "dry"
        print("Soil is dry, please water the plant")
    elif raw_value < WET_THRESHOLD:
        moisture_level = "wet"
        print("Soil is wet, do not water the plant")
    else:
        moisture_level = "moist"
        print("Soil is moist, no need to water the plant")        # print the raw adc value 
    
    with open(file_path,"a") as file:
        file.write(f"Soil Moisture: {moisture_level} ADC Value: {raw_value} {datetime.now().strftime('%Y/%m/%d %H:%M')}\n")

    return moisture_level, raw_value

def capture_moisture_interval(interval, file_path="soil_moisture.txt"):
    while True:
        capture_moisture_once(file_path)
        time.sleep(interval)

def capture_moisture_for_seconds(seconds, file_path="soil_moisture.txt"):
    end_time = time.time() + seconds
    while time.time() < end_time:
        capture_moisture_once(file_path)
        time.sleep(1)
    print("Exiting Program...")


if __name__ == "__main__":
    file_path = "soil_moisture.txt"
    capture_moisture_for_seconds(10, file_path)


