import time
import board
from digitalio import DigitalInOut, Direction, Pull

from pot import Potentiometer
from battery import Battery
from switch import Switch
from rgb_button import RGB_Button
from bluefruit import Bluefruit

external_power = DigitalInOut(board.EXTERNAL_POWER)
external_power.direction = Direction.OUTPUT
external_power.value = True

pot = Potentiometer(board.A0)
bat = Battery(board.A3)
switch = Switch([board.D13,
                 board.D12,
                 board.D11,
                 board.D10,
                 board.D9,
                 board.D6,
                 board.D5,
                 board.SCL])
button = RGB_Button(board.D24, board.D25, board.SCK, board.EXTERNAL_BUTTON)

ble = Bluefruit(board.TX, board.RX)

while True:
    if ble.update():
        print(ble.get_color())
        button.set_rgb_led(ble.get_color())
    
        
    time.sleep(0.1)