import network
import time

ap = network.WLAN(network.AP_IF)
sta = network.WLAN(network.STA_IF)

# Check if configuration exists
try:
    with open('config.txt', 'r') as f:
        credentials = f.read().split('\n')
        ssid = credentials[0]
        password = credentials[1]

        # If so, switch to station mode and connect
        ap.active(False)
        sta.active(True)
        sta.connect(ssid, password)

        while not sta.isconnected():
            time.sleep(1)
except:
    pass
