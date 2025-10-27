from analogio import AnalogIn

class Battery:
    def __init__(self, pin):
        self.pin = AnalogIn(pin)
        
    def read(self):
        return self.pin.value / 65535 * 3.3 * 2