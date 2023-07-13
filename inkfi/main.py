import machine
from machine import Pin, SPI
import epaper2in13b

# Pin assignments for the ePaper display
EPD_PIN_RST = 17
EPD_PIN_DC = 16
EPD_PIN_CS = 5
EPD_PIN_BUSY = 4

# SPI bus configuration
spi = SPI(2, baudrate=2000000, polarity=0, phase=0)
spi.init()

# Create an instance of the ePaper display
epd = epaper2in13b.EPD(spi, EPD_PIN_CS, EPD_PIN_DC, EPD_PIN_RST, EPD_PIN_BUSY)

# Initialize the ePaper display
epd.init()

# Clear the display
epd.clear()

# Set up a sample text to be displayed
text = "Hello, world!"

# Display the text on the ePaper display
epd.set_font(epaper2in13b.FONT_DEFAULT, size=16)
epd.set_text_color(epaper2in13b.BLACK)
epd.set_background_color(epaper2in13b.WHITE)
epd.set_text_position(10, 10)
epd.write_text(text)

# Update the display
epd.display()

# Put the ESP32 into deep sleep mode to conserve power (optional)
machine.deepsleep()
