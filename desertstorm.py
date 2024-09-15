import time
import board
import neopixel

# Set up the onboard NeoPixel (RGB LED)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# Colors (R, G, B)
CALM_COLOR = (255, 223, 186)  # A warm beige to represent calm desert
BUILDING_COLOR = (255, 165, 0)  # Orange to show the wind picking up dust
STORM_COLOR = (255, 255, 0)  # Bright yellow for a full sandstorm
PEAK_COLOR = (255, 69, 0)  # Red-orange for the storm at its peak

# Ensure the LED is off at the beginning and between phases
def turn_off_pixel():
    pixel.fill((0, 0, 0))

# Calm phase: gentle glow of warm beige
def calm_phase():
    turn_off_pixel()  # Ensure pixel is off before starting
    pixel.brightness = 0.2
    pixel.fill(CALM_COLOR)
    time.sleep(5)  # Lasts 5 seconds

# Building phase: wind picking up with orange glow
def building_phase():
    turn_off_pixel()  # Ensure pixel is off before starting
    pixel.brightness = 0.4
    for i in range(10):
        pixel.fill(BUILDING_COLOR)
        time.sleep(0.5)
        pixel.brightness -= 0.02  # Simulate gusts of wind by dimming slightly

# Storm phase: fast flashing to represent chaos of sandstorm
def storm_phase():
    turn_off_pixel()  # Ensure pixel is off before starting
    pixel.brightness = 0.7
    for i in range(40):  # Increased iterations for a longer storm
        pixel.fill(STORM_COLOR)
        time.sleep(0.1)  # Flash duration for storm color
        pixel.fill(PEAK_COLOR)
        time.sleep(0.1)  # Flash duration for peak color

# Main animation
def desert_storm():
    calm_phase()        # Calm before the storm (5 seconds)
    building_phase()    # Wind picking up (5 seconds)
    storm_phase()       # Full storm (8 seconds)

# Run the animation to simulate the desert storm
while True:
    desert_storm()
    time.sleep(10)  # Wait before the next storm

