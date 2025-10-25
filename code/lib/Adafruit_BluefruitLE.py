class Adafruit_BluefruitLE:
    def __init__(self, uart):
        self.uart = uart

    def connect(self):
        print(f"Connecting to {self.name} at {self.address}...")
   

    def disconnect(self):
        print(f"Disconnecting from {self.name}...")

    def read_data(self):
        print(f"Reading data from {self.name}...")
        return "Sample Data"

    def write_data(self, data):
        print(f"Writing data to {self.name}: {data}")