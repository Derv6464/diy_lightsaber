import neopixel
import time

class Ring:
    def __init__(self, pin, num_pixels=16):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=True)
        self.pixels.brightness = 0.1
        
    def set_color(self, color):
        for i in range(self.num_pixels):
            self.pixels[i] = color
            self.pixels.show()
            
            time.sleep(0.2)
            