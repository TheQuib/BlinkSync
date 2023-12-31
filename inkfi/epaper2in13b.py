from micropython import const
import framebuf

# Display resolution
EPD_WIDTH = const(122)
EPD_HEIGHT = const(250)

# Color definitions
BLACK = const(0)
WHITE = const(1)
RED = const(2)

class EPD:
    def __init__(self, spi, cs_pin, dc_pin, rst_pin, busy_pin):
        self.spi = spi
        self.cs_pin = cs_pin
        self.dc_pin = dc_pin
        self.rst_pin = rst_pin
        self.busy_pin = busy_pin
        self.buffer = bytearray((EPD_WIDTH // 8) * EPD_HEIGHT)
        self.framebuf = framebuf.FrameBuffer(self.buffer, EPD_WIDTH, EPD_HEIGHT, framebuf.MONO_HLSB)

    def _command(self, command):
        self.dc_pin.value(0)
        self.cs_pin.value(0)
        self.spi.write(bytearray([command]))
        self.cs_pin.value(1)

    def _data(self, data):
        self.dc_pin.value(1)
        self.cs_pin.value(0)
        self.spi.write(data)
        self.cs_pin.value(1)

    def init(self):
        self.reset()
        self._command(0x01)  # Driver output control
        self._data(bytearray([(EPD_HEIGHT - 1) & 0xFF, ((EPD_HEIGHT - 1) >> 8) & 0xFF, 0x00]))  # 250-1
        # Other initialization commands go here

    def reset(self):
        self.rst_pin.value(0)
        self.rst_pin.value(1)

    def wait_until_idle(self):
        while self.busy_pin.value() == 0:
            pass

    def set_font(self, font, size):
        pass  # Placeholder; no font support in this implementation

    def set_text_color(self, color):
        self.framebuf.fill(color)

    def set_text_position(self, x, y):
        self.text_x = x
        self.text_y = y

    def write_text(self, text, x, y):
        self.framebuf.text(text, x, y)

    def display(self):
        self._command(0x24)  # Write RAM
        self._data(self.buffer)
        # Other display update commands go here

    def clear(self):
        self.framebuf.fill(0)
