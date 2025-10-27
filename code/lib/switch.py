from digitalio import DigitalInOut, Direction, Pull

class Switch:
    def __init__(self, pins: list):
        self.pins = []
        
        for pin in pins:
            pin_init = DigitalInOut(pin)
            pin_init.direction = Direction.INPUT
            pin_init.pull = Pull.UP
            self.pins.append(pin_init)
            

    def get_state(self) -> list:
        for i, pin in enumerate(self.pins):
            if not pin.value:
                return i+1
        return 0