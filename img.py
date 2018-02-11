# Display Image

from PIL import Image
from neopixel import *

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
	parser.add_argument('string', type=str, help='Image name')
    	args = parser.parse_args()
	if args.c:
		signal.signal(signal.SIGINT, signal_handler)
	if args.string:
		return args.string
	else:
		return 'Logo.png'


# LED strip configuration:
LED_COUNT = 100  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB  # Strip type and colour ordering

size = 10,10

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


def printImage(img):
	img = img.resize((10, 10), Image.ANTIALIAS)
	rgb_img = img.convert('RGB')

	pixel = [[[0,0,0] for i in range(10)] for j in range(10)];

	pixel[9][9][2] = "Test"

	for y in range(10):
    		for x in range(10):
			r, g, b = rgb_img.getpixel((y, x))
			#pixel[y][x][0], pixel[9][9][1], pixel[9][9][2] = rgb_img.getpixel((y, x))
			setPixel(strip, y*10+x, Color(r, g, b))
			strip.show()


if __name__ == '__main__':
    # Process arguments
    	path = opt_parse()


	# Create NeoPixel object with appropriate configuration.
    	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    	# Intialize the library (must be called once before other functions).
    	strip.begin()

	img = Image.open('image/%s'%(path))

	if path[-1] == 'f':
		i = 0
            	while 1:
                	printImage(img)
            		i += 1
            		img.seek(img.tell() + 1)
	else:
		printImage(img)
