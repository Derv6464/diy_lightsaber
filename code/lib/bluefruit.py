import busio

class Bluefruit:
    def __init__(self, tx, rx):
        self.uart = busio.UART(tx, rx, baudrate=9600)
        self.last_color = (0,0,0)
        
    def update(self):
        data = self.uart.read(6) 
        if data:
            return self.parse_packet(data)
                
        return False
        
    def parse_packet(self, packet):
        if packet[0] == ord('!') and packet[1] == ord('C'):
            r, g, b = packet[2], packet[3], packet[4]
            checksum = packet[5]
            
            xsum = sum(packet[:-1]) & 0xFF
            xsum = (~xsum) & 0xFF
            
            if xsum == checksum:
                self.last_color = (r, g, b )
            
            return True
        
        return False
        
    def get_color(self):
        return self.last_color