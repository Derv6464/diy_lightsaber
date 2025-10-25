class Switch:
    def __init__(self, pins: list):
        self.pins = pins

        for pin in self.pins:
            pin.setup_input()

    def get_state(self) -> list:
        for pin,i in enumerate(self.pins):
            if pin.read() == 1:
                return i+1
        return 0