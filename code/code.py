import time
import board

from pot import Potentiometer
from battery import Battery
from switch import Switch

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


while True:
    print(switch.get_state())
    time.sleep(1)