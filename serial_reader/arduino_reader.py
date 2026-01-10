import time
from serial import Serial

class ArduinoReader:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.serial = None

    def connect(self):
        self.serial = Serial(self.port, self.baud_rate, timeout=1)
        time.sleep(2)
        print("Свързано с Arduino")

    def read_value(self):
        try:
            line = self.serial.readline().decode().strip()
            return int(line)
        except:
            return None

    def close(self):
        if self.serial:
            self.serial.close()
