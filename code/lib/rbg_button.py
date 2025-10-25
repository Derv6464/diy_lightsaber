class Button(self, r,g,b, button):
    def __init__(self, r_pin, g_pin, b_pin, button_pin):
        self.r_pin = r_pin
        self.g_pin = g_pin
        self.b_pin = b_pin
        self.button_pin = button_pin
        self.r = 0
        self.g = 0
        self.b = 0
        self.button_state = False

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        