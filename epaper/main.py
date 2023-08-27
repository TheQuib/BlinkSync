from machine import Pin, SPI
import uQR
import framebuf
import epaper2in13b

# Configure SPI
spi = SPI(1, baudrate=2000000, polarity=0, phase=0)
spi.init()

# Configure e-paper display
cs = Pin(15, Pin.OUT)
dc = Pin(27, Pin.OUT)
rst = Pin(26, Pin.OUT)
busy = Pin(25, Pin.OUT)
display = epaper2in13b.EPD(spi, cs, dc, rst, busy)

display.init()

# Generate QR code
qr = uQR.QRCode(version=5, error_correction=uQR.ERROR_CORRECT_L)
qr.add_data('https://quibtech.com')
qr.make()

modules = qr.get_matrix()
dim = len(modules)

# Create a new buffer the size of the QR code
buffer = bytearray(dim * dim // 8)
fb = framebuf.FrameBuffer(buffer, dim, dim, framebuf.MONO_HLSB)

# Iterate over QR code and set pixels in buffer accordingly
for y in range(dim):
    for x in range(dim):
        fb.pixel(x, y, int(modules[x][y]))

# Clear the display
display.clear()

# Set the QR code buffer to the display
display.set_frame_memory(fb, 0, 0)

# Update the display
display.display()
