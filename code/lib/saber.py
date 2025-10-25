class Saber:
    def __init__(self, neopixel):
        self.neopixel = neopixel

    def set_color(self, r, g, b):
        for i in range(len(self.neopixel)):
            self.neopixel[i] = (r, g, b)
        self.neopixel.show()

    def cool_on_effect():
        pass

    def cool_off_effect():
        pass

    def swing():
        pass