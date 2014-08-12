#!/usr/bin/env python

import RPi.GPIO as GPIO
import mpr121
import time

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

GPIO.setup(12, GPIO.OUT)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# Track touches

touches = [0];

# initialize light
is_led_on = False

while True:

	if (GPIO.input(7)): # Interupt pin is high
		pass
	else: # Interupt pin is low

		touchData = mpr121.readData(0x5a)

		for i in range(1):
			if (touchData & (1<<i)):

				if (touches[i] == 0):

					print( 'Pin ' + str(i) + ' was just touched')

					if (i == 0):
						is_led_on = not is_led_on
						GPIO.output(12,is_led_on)
						time.sleep(.3)
											
					#else:
					#	GPIO.output(12,is_led_on)

				touches[i] = 1;
			else:
				if (touches[i] == 1):
					is_led_on = not is_led_on
					print( 'Pin ' + str(i) + ' was just released')
					GPIO.output(12, is_led_on)
					time.sleep(.30)
				touches[i] = 0;
