import sys
import usb.core
import usb.util

from array import array

from WeDoDefs import *

WeDo = usb.core.find(idVendor=0x0694, idProduct=0x0003)

if WeDo is None:
	sys.exit("Can't find Lego WeDo")

if WeDo.is_kernel_driver_active(0):
	try:
		WeDo.detach_kernel_driver(0)
	except usb.core.USBError as e:
		sys.exit("Could not detatch kernel driver: %s" % str(e))

endpoint = WeDo[0][(0,0)][0]

data  = endpoint.read(32)[-8:]

endpoint.write(array("B", [0x40, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))

print(data)
