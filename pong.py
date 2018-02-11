# Pong

#from neopixel import *
import random
import time

import argparse
import signal
import sys


def signal_handler(signal, frame):
    	colorWipe(strip, Color(0, 0, 0))
    	sys.exit(0)


def opt_parse():
   	parser = argparse.ArgumentParser()
    	parser.add_argument('-c', action='store_true', help='clear the display on exit')
    	args = parser.parse_args()
    	if args.c:
        	signal.signal(signal.SIGINT, signal_handler)


# LED strip configuration:
LED_COUNT = 100  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
#LED_STRIP = ws.WS2811_STRIP_GRB  # Strip type and colour ordering

# Pong Variables
posPlayer = 1
posKI = 4
posBall = 54
playerLength = 8


# Output Data
def setPixel(strip, id, color):
    	y = id / 10
    	x = id - (y * 10)
    	if y % 2 != 0:
        	x = 9 - x
    	led = (y * 10) + x
    	strip.setPixelColor(led, color)

def cleanPixel(strip):
    	for i in range(strip.numPixels()):
        	print(i)
        	strip.setPixelColor(i, Color(0, 0, 0))
    	strip.show()


def runPong(strip):
   	for i in range(playerLength):
        	setPixel(strip, posPlayer + i, Color(0, 255, 0))
    	for y in range(3):
        	setPixel(strip, 90 + posKI + y, Color(0, 0, 255))

    	setPixel(strip, posBall, Color(255, 0, 0))
    	strip.show()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    	opt_parse()

    # Create NeoPixel object with appropriate configuration.
    	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    	strip.begin()

    	runPong(strip)



