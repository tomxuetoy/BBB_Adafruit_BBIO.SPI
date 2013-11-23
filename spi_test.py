#import the library
from Adafruit_BBIO.SPI import SPI

#Only need to execute one of the following lines:
#spi = SPI(bus, device) #/dev/spidev<bus>.<device>
spi = SPI(0,0)  #/dev/spidev1.0
spi = SPI(0,1)  #/dev/spidev1.1
spi = SPI(1,0)  #/dev/spidev2.0
spi = SPI(1,1)  #/dev/spidev2.1

# root@beaglebone:~/tomxue# python spi_test.py
# [  408.353709] bone-capemgr bone_capemgr.9: slot #9: ADAFRUIT-SPI1 conflict P9.31 (#5:BB-BONELT-HDMI)
# [  408.363179] bone-capemgr bone_capemgr.9: slot #9: Failed verification
# Traceback (most recent call last):
#   File "spi_test.py", line 8, in <module>
#     spi = SPI(1,0)      #/dev/spidev2.0
# IOError: [Errno 2] No such file or directory
