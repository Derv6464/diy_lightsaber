import adafruit_lis3dh
from digitalio import DigitalInOut, Direction, Pull

class Accelerometer:
    HIT_THRESHOLD = 120
    SWING_THRESHOLD = 130
    
    def __init__(self, i2c, int1):
        int1 = DigitalInOut(int1)
        self.lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
        # Accelerometer Range (can be 2_G, 4_G, 8_G, 16_G)
        self.lis3dh.range = adafruit_lis3dh.RANGE_2_G
        self.lis3dh.set_tap(1, self.HIT_THRESHOLD)
        
    def get_total_accel(self):
        x, y, z = self.lis3dh.acceleration
        return x * x + z * z
    
    def tapped(self):
        return self.lis3dh.tapped
