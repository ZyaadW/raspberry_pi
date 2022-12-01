import spidev
import time

spi = spidev.Spidev()
spi.open(0,0)
spi.max_speed_hz = 100000

def readSPI (channel):
    adc = spi.xfer2 ([1, (8+channel) <<4,0])
    data = ((adc[1] & 3) <<8) +adc[2]
    return(data)

channelPot = 0

while(True):
    waarde_pot = readSPI (channelPot)
    print (waarde_pot)
    time.sleep(0.1)

