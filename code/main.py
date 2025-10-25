import Neopixel
import adafruit_ble
import busio
import board
from switch_eight import Switch

ble_uart = busio.UART(tx=board.TX, rx=board.RX, baudrate=9600)
bluetooth = adafruit_ble.BLERadio()
switch = Switch(pins=[board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9])

saber = Neopixel.NeoPixel(pin=5, num_pixels=60, brightness=0.5)
ring = Neopixel.NeoPixel(pin=6, num_pixels=12, brightness=0.7)

action_mode = ActionMode(saber=saber, button=button, speaker=speaker)
walllight_mode = WallLightMode(ring=ring, sensor=light_sensor, bluetooth=bluetooth)

while True:
    if switch.get_state() == 1:
        action_mode.run()
    elif switch.get_state() == 2:
        walllight_mode.run()