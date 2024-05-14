from picamera2 import Picamera2
from time import sleep

camera = Picamera2()


def capture_photo(resolution, file_path):
    camera.resolution = resolution 
    camera.framerate = 60 # Set the frame rate to 60 fps.

    camera.start() # Start the camera
    sleep(5) # Allow the camera to warm up
    camera.capture_file(file_path) # Save the photo to the specified file path
    camera.stop() # Stop the camera
    print("Photo captured successfully!")

if __name__ == "__main__":
    capture_photo((640, 480), "image.jpg")
    print("Exiting Program...")