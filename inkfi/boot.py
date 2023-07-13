# This is script that run when device boot up or wake from sleep.


import main
from main import epd2in13b as epd3in13b

epd = epd3in13b()
epd.init()
epd.Clear()
epd.sleep()