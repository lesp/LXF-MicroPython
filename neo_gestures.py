from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 24)

while True:
    reading_x = accelerometer.get_x()
    if reading_x < 0:
        reading_x = 0
    reading_x = int(reading_x /10)
    reading_y = accelerometer.get_y()
    reading_y = int(reading_y /10)
    if reading_y < 0:
        reading_y = 0
    reading_z = accelerometer.get_z()
    reading_z = int(reading_z /10)
    if reading_z < 0:
        reading_z = 0
    print(reading_x,reading_y,reading_z)
    for i in range(24):
        red = reading_x
        green = reading_y
        blue = reading_z
        np[i] = (red, green, blue)
        np.show()