import machine
import epaper2in13b
import framebuf

# Pin definitions
CS_PIN = machine.Pin(15, machine.Pin.OUT)
DC_PIN = machine.Pin(27, machine.Pin.OUT)
RST_PIN = machine.Pin(26, machine.Pin.OUT)
BUSY_PIN = machine.Pin(25, machine.Pin.IN)

# SPI initialization
spi = machine.SPI(1, baudrate=115200, polarity=0, phase=0)

# Initialize ePaper display
epaper = epaper2in13b.EPD(spi, CS_PIN, DC_PIN, RST_PIN, BUSY_PIN)
epaper.init()

# Set font and text color
size = 16
epaper.set_font(framebuf.MONO_HMSB, size)
epaper.set_text_color(epaper2in13b.BLACK)

# Set text position and write text
x = 10
y = 10
epaper.set_text_position(x, y)
epaper.write_text("Hello, World!", x, y)

# Display the content on the ePaper display
epaper.display()
