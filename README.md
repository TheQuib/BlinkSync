# inkfi
Inkfi - E-Paper driven WiFi QR code display

# Prerequisites
 - ESP32 OTA

# Gotchas
If you're on Linux, I found I needed to give myself ownership in order to interact via serial connection with the ESP32.

This can be done with the following command:
```bash
sudo chmod a+rw /dev/ttyUSB0
```