class ActionMode:
    def __init__(self, saber, button, speaker):
        self.saber = saber
        self.button = button
        self.speaker = speaker

    def run(self):
        #code from adafruit saber code
        if self.button.is_pressed():
            self.saber.set_color(255, 0, 0)  # Set saber color to red
            self.speaker.play_sound("activation_sound.wav")  # Play activation sound
        else:
            self.saber.set_color(0, 0, 0)  # Turn off saber color


        
