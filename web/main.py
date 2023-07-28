import network
import socket
import ure
import machine
import json
import time

ap_ssid = 'ESP32'
ap_password = '12345678'

ap = network.WLAN(network.AP_IF)
sta = network.WLAN(network.STA_IF)

def url_decode(url):
    return ure.sub('%20', ' ', url)

def handle_request(request):
    header, body = request.split('\r\n\r\n', 1)
    headers = header.split('\r\n')[1:]
    method, path, protocol = header.split('\r\n')[0].split(' ')

    # Handle form submission
    if method == 'POST' and path == '/configure':
        ssid = url_decode(ure.search("ssid=(.*)&password", body).group(1))
        password = url_decode(ure.search("password=(.*)", body).group(1))

        with open('config.txt', 'w') as f:
            f.write(ssid + '\n' + password)

        return 'HTTP/1.0 200 OK\r\n\r\nPlease wait while we try to connect to the WiFi network.'

    if method == 'GET' and path == '/scan':
        sta.active(True)
        networks = sta.scan()
        sta.active(False)
        return 'HTTP/1.0 200 OK\r\n\r\n' + json.dumps([n[0].decode('utf-8') for n in networks])

    with open('index.html', 'r') as f:
        html = f.read()
    return 'HTTP/1.0 200 OK\r\n\r\n' + html

def start_server():
    s = socket.socket()
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print('Content = %s' % request)

        response = handle_request(request.decode('utf-8'))
        conn.send(response)
        conn.close()

        # If config exists, try to connect
        try:
            with open('config.txt', 'r') as f:
                ssid, password = f.read().split('\n')
                sta.active(True)
                sta.connect(ssid, password)
                for _ in range(20):  # Wait for up to 20 seconds
                    if sta.isconnected():
                        machine.reset()
                    time.sleep(1)
                sta.active(False)
        except:
            pass

ap.active(True)
ap.config(essid=ap_ssid, password=ap_password)
start_server()
