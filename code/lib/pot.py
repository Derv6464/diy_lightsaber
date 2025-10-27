from analogio import AnalogIn

class Potentiometer:
    def __init__(self, pin):
        self.pin = AnalogIn(pin)
        
    def read(self):
        return self.pin.value