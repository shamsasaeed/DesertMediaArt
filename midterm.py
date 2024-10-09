import time
import board
import neopixel
from analogio import AnalogIn
import digitalio
from rainbowio import colorwheel

# Setup for NeoPixel Ring power (D10 to enable power)
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True  # Enable power to NeoPixels

# NeoPixel Ring setup
NUM_PIXELS = 12  # NeoPixel ring length
BRIGHTNESS = 0.25  # Set to 25% brightness
pixel_pin = board.D5  # NeoPixel ring data connected to D5
pixels = neopixel.NeoPixel(pixel_pin, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False)

# Setup for Force Sensor (on A0 pin)
force_sensor = AnalogIn(board.A0)

# Function to read force sensor value
def read_force_sensor():
    return force_sensor.value

# Smooth transition between two colors
def fade_to_color(start_color, end_color, steps=50, delay=0.02):
    for i in range(steps):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / steps)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / steps)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / steps)
        pixels.fill((r, g, b))
        pixels.show()
        time.sleep(delay)

# Color constants (RGB)
DIM_GREY = (50, 50, 50)  # Dimmer grey
DARK_YELLOW = (255, 200, 0)  # Darker yellow
BRIGHT_ORANGE = (255, 100, 0)  # Brighter orange
DARK_ORANGE = (255, 50, 0)  # Even darker orange
RED = (255, 0, 0)

# Initial state
pixels.fill(DIM_GREY)
pixels.show()
touch_count = 0

print("Starting NeoPixel Spider Interaction")

# Main loop
while True:
    # Read the force sensor value
    sensor_value = read_force_sensor()

    # Threshold to detect touch
    if sensor_value > 30000:  # Adjust this value based on testing
        touch_count += 1
        if touch_count == 1:
            # Smooth transition from dim grey to dark yellow
            fade_to_color(DIM_GREY, DARK_YELLOW)
            time.sleep(5)
        elif touch_count == 2:
            # Smooth transition from dark yellow to bright orange
            fade_to_color(DARK_YELLOW, BRIGHT_ORANGE)
            time.sleep(7)
        elif touch_count == 3:
            # Smooth transition from bright orange to dark orange
            fade_to_color(BRIGHT_ORANGE, DARK_ORANGE)
            time.sleep(5)
        elif touch_count == 4:
            # Smooth transition from dark orange to red
            fade_to_color(DARK_ORANGE, RED)
            time.sleep(5)
        elif touch_count == 5:
            # Flash red 40 times very fast
            for _ in range(40):
                pixels.fill(RED)
                pixels.show()
                time.sleep(0.05)  # Very fast blink duration
                pixels.fill((0, 0, 0))  # Off between flashes
                pixels.show()
                time.sleep(0.05)
            # Reset touch count and return to dim grey
            touch_count = 0
            fade_to_color(RED, DIM_GREY)
        # Debouncing to avoid multiple reads
        time.sleep(0.5)

