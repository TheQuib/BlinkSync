import network

wifi_ssid = "No Internet"
wifi_password = "Jersey Shore"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_password)

while not sta_if.isconnected():
    pass

print("Connected to Wi-Fi:", wifi_ssid)
print("IP address:", sta_if.ifconfig()[0])
