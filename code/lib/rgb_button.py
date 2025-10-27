import pwmio
from digitalio import DigitalInOut, Direction, Pull
import simpleio

class RGB_Button:
    def __init__(self, r_pin, g_pin, b_pin, button_pin):
        self.r = pwmio.PWMOut(r_pin)
        self.g = pwmio.PWMOut(g_pin)
        self.b = pwmio.PWMOut(b_pin)
        self.button = DigitalInOut(button_pin)
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.UP

    def set_rgb_led(self, color):
        self.r.duty_cycle = int(simpleio.map_range(color[0], 0, 255, 65535, 0))
        self.g.duty_cycle = int(simpleio.map_range(color[1], 0, 255, 65535, 0))
        self.b.duty_cycle = int(simpleio.map_range(color[2], 0, 255, 65535, 0))
        
    def read():
        return self.button.value
    