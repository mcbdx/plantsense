## Plant Sense Project 

# Importing the necessary libraries
from cam import capture_photo
from soil_moisture import capture_moisture_once
from get_temp import log_temperature_humidity_once


def main():
    print("Starting Plant Sense Program...")

    # Capture a photo
    capture_photo((640, 480), "image.jpg")
    

    # Capture the soil moisture level
    capture_moisture_once("soil_moisture.txt")

    # Capture the temperature and humidity
    log_temperature_humidity_once("temp.txt")

    print("Exiting Program...")

if __name__ == "__main__":
    main()
