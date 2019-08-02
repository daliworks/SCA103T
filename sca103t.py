#!/usr/bin/python

import time
import spidev
import numpy as np 

sens = {
	'SCA103T-D04' : 6554.0
}
spi = spidev.SpiDev()
spi.open(0, 0)              # open(bus, device)

spi.mode = 3
spi.max_speed_hz = 500000  # set transfer speed

while True:
	data=spi.xfer2([0x10, 0x00, 0x00])
	x = (data[1] << 3) + (data[2] >> 5)
	data=spi.xfer2([0x11, 0x00, 0x00])
	y = (data[1] << 3) + (data[2] >> 5)

	out = (x - y) 
	a = np.arcsin(out /sens['SCA103T-D04'])
	d = a / np.pi * 180

	print x, y, d
	time.sleep(1)

spi.close()
